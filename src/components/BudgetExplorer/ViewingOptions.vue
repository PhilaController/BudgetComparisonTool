<template>
  <div class="options-wrapper">
    <div class="my-title">Viewing Options</div>

    <!-- Fiscal year options -->
    <div class="mt-3 fiscal-year-options">
      <div class="my-subtitle text-left">
        Compare to the budget from fiscal year:
      </div>

      <div class="d-flex justify-content-center budget-select-wrapper">
        <v-select
          :items="comparisonFiscalYears"
          v-model="selectedComparisonFiscalYear"
        />
      </div>
    </div>

    <!-- Viewing options -->
    <div class="viewing-options mt-5">
      <div class="my-subtitle">Group circles according to:</div>
      <div class="d-flex flex-column">
        <v-radio-group v-model="selectedViewingOption" class="radio-group">
          <v-radio
            v-for="option in filteredViewingOptions"
            :key="option"
            :label="getAlias(option)"
            :value="option"
            :ripple="false"
          >
          </v-radio>
        </v-radio-group>
        <v-btn
          v-show="selectedViewingOption != null"
          class="reset-button"
          outlined
          :ripple="false"
          @click="resetViewingOption"
        >
          Clear Selection</v-btn
        >
      </div>
    </div>
  </div>
</template>

<script>
import { VRadio, VRadioGroup } from "vuetify/lib";
export default {
  props: [
    "allowedViewingOptions",
    "comparisonFiscalYears",
    "defaultComparisonFiscalYear",
  ],
  components: {
    VRadioGroup,
    VRadio,
  },
  data() {
    return {
      selectedViewingOption: null,
      selectedComparisonFiscalYear: this.defaultComparisonFiscalYear,
      viewingAliases: {
        "By Department": "City Department",
        "All Changes": "All Changes",
        "By Major Class": "Major Class",
        "By Category": "Spending Category",
      },
    };
  },
  computed: {
    filteredViewingOptions() {
      return this.allowedViewingOptions.filter((d) => d != "All Changes");
    },
  },
  methods: {
    getAlias(value) {
      return this.viewingAliases[value];
    },
    resetViewingOption() {
      this.selectedViewingOption = null;
    },
  },
  watch: {
    selectedViewingOption(nextValue) {
      this.$emit("update-viewing-option", nextValue);
    },
    selectedComparisonFiscalYear(nextValue) {
      this.$emit("update-fiscal-year", nextValue);
    },
  },
};
</script>

<style>
.options-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.budget-select-wrapper {
  max-width: 50%;
}
.options-wrapper label {
  margin-bottom: 0rem !important;
  margin-left: 0.25rem;
}

.my-hr {
  margin-top: 1rem !important;
  margin-bottom: 1rem !important;
  border: 0 !important;
  border-top: 2px solid rgba(0, 0, 0, 0.1) !important;
}

.options-wrapper .my-subtitle {
  color: #2c3e50;
  font-weight: 500;
  font-size: 1.15rem;
  text-align: left;
}

.options-wrapper .my-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2c3e50;
}

.reset-button {
  max-width: 250px;
}

.viewing-options {
  min-height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.v-btn:active,
.v-btn:hover,
.v-btn:focus {
  border-color: #000 !important;
  box-shadow: none !important;
  outline: none;
}

@media screen and (max-width: 768px) {
  .budget-select-wrapper {
    max-width: 90%;
  }
  .reset-button {
    max-width: 90%;
  }
  .viewing-options,
  .options-wrapper {
    align-items: center;
  }
  .fiscal-year-options {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
<template>
  <div class="options-wrapper">
    <div class="title">Viewing Options</div>
    <!-- Fiscal year options -->
    <div class="mt-3">
      <div class="subtitle">Compare to the budget from Fiscal Year:</div>
      <div class="d-flex justify-content-center">
        <v-radio-group row v-model="selectedComparisonFiscalYear">
          <v-radio
            v-for="option in comparisonFiscalYears"
            :key="option"
            :label="`${option}`"
            :value="option"
            :ripple="false"
          >
          </v-radio>
        </v-radio-group>
      </div>
    </div>
    <hr class="my-hr" />
    <!-- Viewing options -->
    <div class="viewing-options">
      <div class="subtitle">Group circles according to:</div>
      <div class="d-flex justify-content-center flex-column align-items-center">
        <v-radio-group row v-model="selectedViewingOption" class="radio-group">
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
  props: ["allowedViewingOptions", "comparisonFiscalYears"],
  components: {
    VRadioGroup,
    VRadio,
  },
  data() {
    return {
      selectedViewingOption: null,
      selectedComparisonFiscalYear: this.comparisonFiscalYears[0],
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
    selectedViewingOption(nextValue, prevValue) {
      this.$emit("update-viewing-option", nextValue);
    },
    selectedComparisonFiscalYear(nextValue, prevValue) {
      this.$emit("update-fiscal-year", nextValue);
    },
  },
};
</script>

<style>
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

.options-wrapper .subtitle {
  color: #2c3e50;
  font-weight: 500;
  font-size: 1.15rem;
}

.options-wrapper .title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2c3e50;
}

.reset-button {
  max-width: 250px;
}

.viewing-options {
  min-height: 200px;
}

.v-btn:active,
.v-btn:hover,
.v-btn:focus {
  border-color: #000 !important;
  box-shadow: none !important;
  outline: none;
}

@media screen and (max-width: 768px) {
  .viewing-options .v-input--radio-group__input {
    flex-direction: column !important;
  }
}
</style>
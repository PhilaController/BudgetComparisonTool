<template>
  <!-- Outside wrapper -->
  <div class="budget-explorer-container">
    <!-- User Toolbar -->
    <div class="title d-flex justify-content-center">Budget Explorer</div>
    <div class="title d-flex justify-content-center">
      <div>
        How does the Mayor's Fiscal Year 2022 budget proposal compare to the
        Fiscal Year &nbsp;
        <!-- Year Selection -->
        <Dropdown
          class="title-dropdown"
          ref="fiscalYearDropdown"
          :options="comparisonFiscalYears"
          :defaultValue="selectedComparisonFiscalYear"
          @change="updateYearDropdown($event, 'fiscalYear')"
        />&nbsp;budget?
      </div>
    </div>

    <!-- The total change -->
    <div class="total-change text-center mt-5 pb-5">
      The FY22 budget proposal increases spending by
      <span class="total-change-number">{{ formattedTotalChange }}</span>
      , or
      <span class="total-change-number">{{ formattedPercentTotalChange }}</span
      >, relative to FY{{ selectedComparisonFiscalYear }}'s budget.
    </div>

    <!-- Radio toolbar for different views -->
    <div
      class="budget-explorer-toolbar d-flex align-items-center justify-content-center mt-3"
    >
      <RadioButtonToolbar
        :options="viewingOptions"
        :defaultValue="selectedViewingOption"
        ref="viewingOptionsToolbar"
        @change="setViewingOption"
      />
    </div>

    <!-- Budget Explorer Viz -->
    <BudgetExplorerViz
      class="mt-5"
      :width="totalWidth"
      :currentFiscalYear="currentFiscalYear"
      :selectedComparisonFiscalYear="selectedComparisonFiscalYear"
      :budgetType="budgetType"
      :rawData="rawData"
      :viewingMode="selectedViewingOption"
      :viewingConfig="viewingConfig"
      :tableConfig="tableConfig"
      :legendConfig="legendConfig"
      :annotationLabels="annotationLabels"
      :vizClass="vizClass"
    />
  </div>
</template>

<script>
import * as d3 from "d3";
import Dropdown from "./Dropdown";
import RadioButtonToolbar from "./RadioButtonToolbar";
import BudgetExplorerViz from "./BudgetExplorerViz";
import { formatFn, percentFn } from "@/utils/formatFns";

export default {
  components: { Dropdown, RadioButtonToolbar, BudgetExplorerViz },
  props: [
    "currentFiscalYear",
    "comparisonFiscalYears",
    "budgetType",
    "label",
    "rawData",
    "tableConfig",
    "legendConfig",
    "viewingConfig",
    "viewingOptions",
    "annotationLabels",
    "vizClass",
  ],
  data() {
    return {
      selectedViewingOption: this.viewingOptions[0],
      selectedComparisonFiscalYear: this.comparisonFiscalYears[0],
    };
  },
  mounted() {
    this.updateTotalChangeColor();
  },
  methods: {
    updateTotalChangeColor() {
      // Green or red?
      if (this.totalChange > 0) {
        $(".total-change-number").addClass("green").removeClass("red");
      } else {
        $(".total-change-number").addClass("red").removeClass("green");
      }
    },
    setViewingOption(value) {
      this.selectedViewingOption = value;
    },
    updateYearDropdown(selectedYear, tag) {
      this.selectedComparisonFiscalYear = selectedYear;
      this.updateTotalChangeColor();
    },
  },
  computed: {
    totalWidth() {
      return Math.min(window.screen.width * 0.9, 1000);
    },
    formattedTotalChange() {
      return formatFn(this.totalChange);
    },
    formattedPercentTotalChange() {
      return percentFn(this.percentTotalChange);
    },
    totalChange() {
      let col_new = `${this.currentFiscalYear} (${this.budgetType})`;
      let col_old = `${this.selectedComparisonFiscalYear} (Adopted)`;
      return d3.sum(this.rawData, (d) => d[col_new] - d[col_old]);
    },
    percentTotalChange() {
      let col_old = `${this.selectedComparisonFiscalYear} (Adopted)`;
      return this.totalChange / d3.sum(this.rawData, (d) => d[col_old]);
    },
  },
};
</script>

<style>
.title {
  font-weight: 700;
  font-size: 2.5rem;
}
.title-dropdown > button {
  font-size: 2.5rem;
  background-color: white;
  color: #2176d2 !important;
  margin: 0px;
  padding-top: 0px;
  padding-bottom: 0px;
  border-color: #fff;
  border-width: 2px;
  text-decoration: underline;
}
.title-dropdown .dropdown-item {
  font-size: 2.5rem;
  font-weight: 300;
}
.title-dropdown .dropdown-item:hover {
  color: #2176d2 !important;
  cursor: pointer;
}

.title-dropdown > button:hover,
.title-dropdown > button:focus,
.title-dropdown > button:active {
  background-color: #fff !important;
  color: #2176d2 !important;
  border-width: 0px;
  text-decoration: none;
  border-color: #2176d2;
  border-width: 2px;
  box-shadow: none !important;
}
.total-change {
  font-size: 2rem;
  font-weight: 500;
  border-bottom: 2px solid #deedfc;
}
.total-change2 {
  font-size: 2rem;
  font-weight: 500;
}
.green {
  color: #398649;
}
.red {
  color: #da3b46;
}
</style>
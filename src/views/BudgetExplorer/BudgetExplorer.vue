<template>
  <!-- Outside wrapper -->
  <div class="budget-explorer-container">
    <!-- User Toolbar -->
    <div class="title d-flex justify-content-center">Budget Explorer</div>

    <!-- Budget Explorer Viz -->
    <BudgetExplorerViz
      class="mt-5"
      :width="totalWidth"
      :currentFiscalYear="currentFiscalYear"
      :comparisonFiscalYears="comparisonFiscalYears"
      :budgetType="budgetType"
      :rawData="rawData"
      :viewingConfig="viewingConfig"
      :viewingOptions="viewingOptions"
      :tableConfig="tableConfig"
      :legendConfig="legendConfig"
      :annotationLabels="annotationLabels"
      :vizClass="vizClass"
    />
  </div>
</template>

<script>
import * as d3 from "d3";
import BudgetExplorerViz from "./BudgetExplorerViz";

export default {
  components: { BudgetExplorerViz },
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
  computed: {
    totalWidth() {
      return Math.min(window.screen.width * 0.9, 1000);
    },
  },
};
</script>

<style>
.title {
  font-weight: 700;
  font-size: 2.5rem;
}
</style>
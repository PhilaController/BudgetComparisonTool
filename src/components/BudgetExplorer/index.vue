<template>
  <!-- Outside wrapper -->
  <div class="budget-explorer-container">
    <!-- User Toolbar -->
    <h2 class="app-title d-flex justify-content-center pb-8">
      Budget Explorer
    </h2>

    <!-- Budget Explorer Viz -->
    <BudgetExplorerViz
      class="mt-5"
      :width="totalWidth"
      :currentFiscalYear="currentFiscalYear"
      :startFiscalYear="startFiscalYear"
      :comparisonFiscalYears="comparisonFiscalYears"
      :defaultComparisonFiscalYear="defaultComparisonFiscalYear"
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
import BudgetExplorerViz from "./BudgetExplorerViz";

export default {
  components: { BudgetExplorerViz },
  props: [
    "currentFiscalYear",
    "startFiscalYear",
    "comparisonFiscalYears",
    "defaultComparisonFiscalYear",
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
.app-title {
  font-weight: 600;
  font-size: 2.5rem;
}
</style>

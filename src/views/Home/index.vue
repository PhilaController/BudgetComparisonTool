<template>
  <div class="home-page">
    <div class="intro text-left ml-3 mr-3">
      <p>
        On April 15, 2021, Mayor Kenney released his
        <a
          class="text-link"
          href="https://www.phila.gov/documents/mayor-kenneys-fiscal-year-2022-budget/"
          target="blank_"
          >budget proposal</a
        >
        for the upcoming fiscal year as part of the City’s annual Five Year
        Financial Plan. The budget
      </p>
      <p>
        As part of an
        <a
          class="text-link"
          href="https://controller.phila.gov/philadelphia-audits/covid19-fiscal-impact/"
          target="blank_"
          >ongoing analysis</a
        >
        of the COVID-19 impact on City finances, the City Controller’s Office is
        releasing a tool to visualize and better understand the major changes in
        the newly released budget. The tool is intended to serve as a resource
        for policymakers and Philadelphians alike, bringing necessary
        transparency to the City’s budgeting process.
      </p>

      <p>
        Ultimately, the goal of any city government is to provide vital services
        to residents through the efficient and effective use of taxpayer money.
        At a time of historic unemployment, declining tax revenues and
        unprecedented challenges for local businesses, striving to reach this
        goal through strategic budget decisions is more important than ever.
      </p>

      <p>
        The visualization includes data on planned spending and estimated
        revenue for the City's General Fund for fiscal years 2020 through 2025.
        Spending data can be broken down by fiscal year, City department,
        spending class, and spending category. Additionally, revenue data can be
        viewed by fiscal year and revenue source.
      </p>
    </div>
    <BudgetExplorer
      :currentFiscalYear="2022"
      :comparisonFiscalYears="[2021, 2020]"
      budgetType="Proposed"
      label="spending"
      vizClass="spending-explorer"
      :rawData="rawData"
      :viewingOptions="viewingOptions"
      :viewingConfig="viewingConfig"
      :tableConfig="tableConfig"
      :legendConfig="legendConfig"
      :annotationLabels="annotationLabels"
    />
  </div>
</template>

<script>
import BudgetExplorer from "../BudgetExplorer/BudgetExplorer";
import { percentFn, netChangeFormatFn, formatFn } from "@/utils/formatFns";

export default {
  components: { BudgetExplorer },
  data() {
    return {
      annotationLabels: ["Budget increases", "Budget cuts"],
      viewingOptions: [
        "All Changes",
        "By Department",
        "By Major Class",
        "By Category",
      ],
      tableConfig: {
        grouped: [
          "All Changes",
          "By Department",
          "By Major Class",
          "By Category",
        ],
        groupby: {
          "All Changes": "name",
          "By Department": "name",
          "By Major Class": "major_class_description",
          "By Category": "category_code_description",
        },
        childColumns: {},
        headerColumns: [
          {
            label: "Name",
            field: "name",
            required: true,
          },
          {
            label: "Major Class",
            field: "major_class_description",
            required: true,
          },
          {
            label: "Category",
            field: "category_code_description",
            required: false,
          },
        ],
      },
      rawData: require("@/data/FYP2226-proposed-by-major-class.json"),
    };
  },
  created() {
    // IMPORTANT: make sure FA does not watch SVG elements
    if (window.FontAwesome) {
      window.FontAwesome.config.observeMutations = false;
      window.FontAwesome.config.searchPseudoElements = false;
    }
  },
  computed: {
    smallScreen() {
      return window.screen.width <= 768;
    },
    legendConfig() {
      return {
        sizes: this.smallScreen ? [1e6, 50e6, 100e6] : [1e6, 50e6, 200e6],
        colorScaleDomain: [-1, 1],
        label: "budgeted spending",
      };
    },
    viewingConfig() {
      return {
        "All Changes": {
          columns: 1,
          height: 400,
          force_type: "charge",
          force_strength: 0.3,
        },
        "By Department": {
          columns: this.smallScreen ? 2 : 4,
          height: this.smallScreen ? 3500 : 2500,
          groupby: "dept_name",
          force_type: "collide",
          force_strength: 0.05,
        },
        "By Major Class": {
          columns: this.smallScreen ? 2 : 3,
          height: this.smallScreen ? 750 : 650,
          groupby: "major_class_description",
          force_type: "collide",
          force_strength: 0.05,
        },
        "By Category": {
          columns: this.smallScreen ? 2 : 4,
          height: this.smallScreen ? 1000 : 800,
          groupby: "category_code_description",
          force_type: "collide",
          force_strength: 0.05,
        },
      };
    },
  },
};
</script>


<style scoped>
.intro {
  border-bottom: 2px solid #deedfc;
  margin-bottom: 40px;
}

.intro p {
  text-align: justify;
}
</style>

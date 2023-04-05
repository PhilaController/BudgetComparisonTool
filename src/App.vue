<template>
  <div data-vuetify>
    <v-app id="app">
      <v-main>
        <!-- Intro -->
        <Home />

        <!-- Budget Explorer -->
        <BudgetExplorer
          class="pt-4"
          :currentFiscalYear="currentFiscalYear"
          :startFiscalYear="startFiscalYear"
          :comparisonFiscalYears="comparisonFiscalYears"
          :defaultComparisonFiscalYear="defaultComparisonFiscalYear"
          :budgetType="kind"
          label="spending"
          vizClass="spending-explorer"
          :rawData="rawData"
          :viewingOptions="viewingOptions"
          :viewingConfig="viewingConfig"
          :tableConfig="tableConfig"
          :legendConfig="legendConfig"
          :annotationLabels="annotationLabels"
        />
      </v-main>
    </v-app>
  </div>
</template>

<script>
import BudgetExplorer from "@/components/BudgetExplorer";

export default {
  name: "BudgetComparisonApp",
  components: {
    BudgetExplorer,
    Home: require("@/components/Home/" + __TAG__ + ".vue").default, // eslint-disable-line
  },
  data() {
    return {
      startFiscalYear: 2020,
      currentFiscalYear: parseInt(__FY__), // eslint-disable-line
      kind: __KIND__, // eslint-disable-line
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
            width: "25%",
          },
          {
            label: "Major Class",
            field: "major_class_description",
            required: true,
            width: "25%",
          },
          {
            label: "Category",
            field: "category_code_description",
            required: false,
            width: "25%",
          },
        ],
      },
      rawData: require("@/data/budget-comparison-data.json"),
    };
  },
  computed: {
    smallScreen() {
      return window.screen.width <= 768;
    },
    legendConfig() {
      return {
        sizes: this.smallScreen ? [1e6, 200e6] : [1e6, 50e6, 200e6],
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
          height: this.smallScreen ? 4000 : 3250,
          groupby: "dept_name",
          force_type: "collide",
          force_strength: 0.05,
        },
        "By Major Class": {
          columns: this.smallScreen ? 2 : 3,
          height: this.smallScreen ? 1000 : 1000,
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
    comparisonFiscalYears() {
      let out = [];

      // Add current year proposed budget
      if (this.kind == "Adopted") {
        out.push(this.currentFiscalYear + " (Proposed)");
      }

      // Add past year adopted budgets
      for (
        let fy = this.currentFiscalYear - 1;
        fy >= this.startFiscalYear;
        fy--
      ) {
        out.push(fy + " (Adopted)");
      }

      return out;
    },
    defaultComparisonFiscalYear() {
      if (this.kind == "Adopted") return this.comparisonFiscalYears[1];
      else return this.comparisonFiscalYears[0];
    },
  },
};
</script>

<style>
@media only screen and (max-width: 736px) {
  .header-button-block {
    width: 100%;
  }
}
@media only screen and (min-width: 736px) {
  .entry-header .row:first-child {
    flex-wrap: nowrap;
  }
}
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

#nav a {
  font-weight: bold;
  font-size: 1.2rem;
}
.my-nav-link:not(:last-child) {
  border-right: 2px solid #666;
  padding-right: 0.25rem;
}
.my-nav-link:not(:first-child) {
  padding-left: 0.25rem;
}
.my-nav-link:hover {
  text-decoration: none;
}
#nav a.router-link-exact-active {
  color: #f3c613 !important;
}
#nav a,
.my-nav-link {
  color: #2176d2 !important;
}
.my-nav-link:hover {
  color: #0f4d90 !important;
}
.my-card-title {
  font-size: 1.5rem;
  font-weight: 500;
}
.text-link:hover {
  text-decoration: none;
}
.text-link {
  color: #2176d2 !important;
}
.text-link:hover {
  color: #0f4d90 !important;
}
</style>

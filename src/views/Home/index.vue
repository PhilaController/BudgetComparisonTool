<template>
  <div class="home-page">
    <div class="intro text-left ml-3 mr-3">
      <p>
        On June 24, 2021, City Council approved the budget for Fiscal Year 2022
        (FY22) as part of the City’s annual Five Year Financial Plan. While the
        COVID-19 pandemic is still impacting the City’s finances, the adopted
        FY22 budget includes an overall increase in spending due to $1.4 billion
        in federal funding the City is receiving as part of the American Rescue
        Plan. Without this federal funding, the City was once again facing a
        <a
          class="text-link"
          href="https://controller.phila.gov/philadelphia-audits/covid19-fiscal-impact-mar-2021/"
          target="blank_"
          >large revenue shortfall</a
        >
        that would have necessitated significant spending reductions. These cuts
        would have been in addition to those enacted as part of last year's
        budget, when the
        <a
          href="https://controller.phila.gov/philadelphia-audits/interactive-fy21-budget/"
          class="text-link"
          target="blank_"
          >City's FY21 budget</a
        >
        decreased by more than 4 percent as revenues declined as a result of the
        pandemic's impact on the local economy.
      </p>
      <p>
        With the help of the additional federal funding, the adopted FY22 budget
        restores many, but not all, of the pandemic-related spending cuts. To
        better understand these changes, the City Controller’s Office is
        releasing a tool to visualize the major changes in the newly released
        budget relative to budgets from previous years. The tool is intended to
        serve as a resource for policymakers and Philadelphians alike, bringing
        necessary transparency to the City’s budgeting process.
      </p>

      <h3>About this tool</h3>

      <p>
        The visualization includes budgeted spending data for the
        <a
          class="text-link"
          href="https://controller.phila.gov/wp-content/uploads/2021/06/FY22-26-Adopted.pdf"
          target="blank_"
        >
          <b>FY22 Adopted Budget</b></a
        >. Users can explore the adopted FY22 budget by comparing to the
        original FY22 proposal as well as the adopted budgets from the past two
        fiscal years:
      </p>
      <ul class="indented">
        <li>
          <a
            href="https://www.phila.gov/media/20210414133527/FY22-Budget-in-Brief-Proposed-FINAL.pdf"
            class="text-link"
            targert="blank_"
            ><b>The FY22 Proposed Budget</b></a
          >: Proposed by the Mayor in April 2021, this budget proposal includes
          overall spending increases due to the federal relief from the American
          Rescue Plan;
        </li>
        <li>
          <a
            href="https://www.phila.gov/finance/pdfs/Operating%20Budget/FY21_Budget_in_Brief_Adopted_FINAL.pdf"
            class="text-link"
            targert="blank_"
            ><b>The FY21 Adopted Budget</b></a
          >: Adopted by City Council in June 2020, this budget includes spending
          cuts due to the impact of the COVID-19 pandemic; and
        </li>
        <li>
          <a
            href="https://www.phila.gov/finance/pdfs/Operating%20Budget/FY20%20BudgetinBrief_Adopted.pdf"
            class="text-link"
            target="blank_"
            ><b>The FY20 Adopted Budget</b></a
          >: Adopted by City Council in June 2019, this budget is the best
          representation of City spending prior to the COVID-19 pandemic.
        </li>
      </ul>
      <p>
        Spending changes are broken down by City department as well as the
        "major class" associated with each type of spending. The City uses seven
        major classes to classify spending:
      </p>
      <ul class="indented">
        <li><b>Personal Services</b>: Payroll for City employees;</li>
        <li>
          <b>Purchase of Services</b>: Spending on contracts and leases with
          outside vendors, which includes spending on professional services;
        </li>
        <li>
          <b>Materials/Equip.</b>: Spending on materials, equipment, and other
          supplies needed by City departments;
        </li>
        <li>
          <b>Debt Service</b>: Fixed payments on previously-issued City debt
          obligations;
        </li>
        <li>
          <b>Contrib./Indemnities</b>: Spending on educational and nonprofit
          contributions as well as indemnities (lawsuits against the City). For
          example, this class includes the City's annual contributions to the
          School District and Community College of Philadelphia; and
        </li>
        <li>
          <b>Advances & Misc.</b>: In addition to miscellaneous spending, this
          class includes funding held in reserve to prepare for future
          recessions or unanticipated expenditures.
        </li>
      </ul>
      <p>
        In addition to viewing all changes at once, users can group the changes
        according to department, major class, or spending category. The spending
        category is a broad label based on the primary function of a department,
        such as Public Safety, Education, and Recreation, Arts, and Culture.
        Budgeted spending items that are outside the main function of a
        department may not be reflected in these spending categories. For
        example, spending on the Philadelphia Cultural Fund was transferred to
        the Managing Director's Office (categorized as "Finance &
        Administration") in the FY21 budget.
      </p>
    </div>
    <BudgetExplorer
      :currentFiscalYear="2022"
      :comparisonFiscalYears="[
        '2022 (Proposed)',
        '2021 (Adopted)',
        '2020 (Adopted)',
      ]"
      :defaultComparisonFiscalYear="'2021 (Adopted)'"
      budgetType="Adopted"
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
      rawData: require("@/data/FYP2226-adopted-by-major-class.json"),
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
          height: this.smallScreen ? 3500 : 2500,
          groupby: "dept_name",
          force_type: "collide",
          force_strength: 0.05,
        },
        "By Major Class": {
          columns: this.smallScreen ? 2 : 3,
          height: this.smallScreen ? 750 : 800,
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

.intro li {
  text-align: justify;
}

.indented {
  margin-left: 5rem;
}

li {
  margin-bottom: 5px;
}

@media screen and (max-width: 768px) {
  .indented {
    margin-left: 2rem;
  }
}
</style>

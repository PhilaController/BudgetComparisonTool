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
        for fiscal year 2022 (FY22) as part of the City’s annual Five Year
        Financial Plan. While the COVID-19 pandemic is still impacting the
        City’s finances, the budget proposal includes an overall increase in
        spending due to an estimated $1.4 billion in federal funding the City is
        set to receive as part of the American Rescue Plan. Without this federal
        funding, the City was once again facing a
        <a
          class="text-link"
          target="blank_"
          href="https://controller.phila.gov/philadelphia-audits/covid19-fiscal-impact-mar-2021/"
          >large revenue shortfall</a
        >
        that would have necessitated significant spending reductions. These cuts
        would have been in addition to those enacted as part of last year's
        budget, when the City's
        <a
          class="text-link"
          target="blank_"
          href="https://controller.phila.gov/philadelphia-audits/interactive-fy21-budget/"
          >FY21 budget</a
        >
        decreased by more than 4 percent as revenues declined as a result of the
        pandemic's impact on the local economy.
      </p>
      <p>
        With the help of the additional federal funding, the Mayor's budget
        proposal restores many, but not all, of the pandemic-related spending
        cuts. To better understand these changes, the City Controller’s Office
        is releasing a tool to visualize the major changes in the newly released
        budget relative to budgets from previous years. The tool is intended to
        serve as a resource for policymakers and Philadelphians alike, bringing
        necessary transparency to the City’s budgeting process.
      </p>

      <h2 class="mb-3">About this tool</h2>

      <p>
        The visualization includes budgeted spending data for the
        <a
          class="text-link"
          target="blank_"
          href="https://www.phila.gov/media/20210414133527/FY22-Budget-in-Brief-Proposed-FINAL.pdf"
          ><b>FY22 Proposed Budget</b></a
        >. Users can explore the new budget proposal by comparing to the adopted
        budgets from the past two fiscal years:
      </p>
      <ul class="indented">
        <li>
          <a
            class="text-link"
            target="blank_"
            href="https://www.phila.gov/media/20210709120156/budget-in-brief-FY2021-approved.pdf"
            ><b>FY21 Adopted Budget</b></a
          >: Adopted by City Council in June 2020, this budget includes spending
          cuts due to the impact of the COVID-19 pandemic; and
        </li>
        <li>
          <a
            class="text-link"
            target="blank_"
            href="https://www.phila.gov/media/20201020113701/budget-in-brief-FY2020-approved.pdf"
            ><b>FY20 Adopted Budget</b></a
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
        such as Public Safety; Education; and General Government. Budgeted
        spending items that are outside the main function of a department may
        not be reflected in these spending categories. For example, spending on
        the Philadelphia Cultural Fund was transferred to the Managing
        Director's Office, which is categorized as "General Government".
      </p>
    </div>
  </div>
</template>

<script>
export default { name: "Home" };
</script>


<style scoped>
.intro {
  border-bottom: 2px solid #deedfc;
  margin-bottom: 40px;
}

.intro p {
  text-align: left;
}

.intro li {
  text-align: left;
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

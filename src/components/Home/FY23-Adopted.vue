<template>
  <div class="home-page">
    <div class="intro text-left ml-3 mr-3">
      <p>
        On June 23, 2022, City Council approved the budget for fiscal year 2023
        (FY23) as part of the City’s annual Five Year Financial Plan. The
        adopted budget totals $5.8 billion in spending and includes an overall
        increase in spending of $571 million (+11%) relative to the adopted FY22
        budget. With the COVID-19 pandemic still impacting the local economy and
        tax revenue totals below pre-pandemic forecasts, this increase in
        spending would not have been possible without $1.4 billion in federal
        relief from the American Rescue Plan. The adopted FY23 budget uses $335
        million of these federal funds during FY23.
      </p>
      <p>
        To better understand the City's finances, the City Controller’s Office
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
          href="https://www.phila.gov/media/20220701112818/FY2023-2027-Five-Year-Plan-per-Council-Approved-Budget.pdf"
          target="blank_"
        >
          <b>FY23 Adopted Budget</b></a
        >. Users can explore the adtoped FY23 budget by comparing to the adopted
        budgets since FY20:
      </p>
      <ul class="indented">
        <li>
          <a
            class="text-link"
            href="https://www.phila.gov/media/20220331104852/Mayors-Operating-Budget-in-Brief-for-FY2023-Proposed-to-the-Council-in-March-2022.pdf"
            target="blank_"
          >
            <b>The FY23 Proposed Budget</b></a
          >: This year's original budget proposal, as released by the Mayor's
          Office on March 31, 2022;
        </li>
        <li>
          <a
            href="https://www.phila.gov/media/20210709120158/budget-in-brief-FY2022-approved.pdf"
            class="text-link"
            targert="blank_"
            ><b>The FY22 Adopted Budget</b></a
          >: Adopted by City Council in June 2021, this budget includes overall
          spending increases due to the federal relief from the American Rescue
          Plan;
        </li>
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
        "major class" associated with each type of spending. The City uses six
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

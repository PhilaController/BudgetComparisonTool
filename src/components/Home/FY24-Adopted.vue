<template>
  <div class="home-page">
    <div class="intro text-left ml-3 mr-3 pb-6">
      <p>
        On June 22, 2023, City Council approved the budget for fiscal year 2024
        (FY24) as part of the City’s annual Five Year Financial Plan. The
        adopted budget totals $6.2 billion in spending and includes an overall
        increase in spending of $353 million relative to the adopted FY23
        budget. In the wake of the COVID-19 pandemic, the City's spending
        continues to increase, supported by $1.4 billion in federal relief from
        the American Rescue Plan. The City will use $391 million of these
        federal funds during FY24, after using $250 million in FY22 and $335
        million in FY23.
      </p>
      <p>
        To better understand the FY24 budget, the City Controller’s Office is
        releasing a tool to visualize the major changes in the newly released
        budget relative to budgets from previous years. The tool is intended to
        serve as a resource for policymakers and Philadelphians alike, bringing
        necessary transparency to the City’s budgeting process.
      </p>

      <h3 class="mb-3 mt-8">About this tool</h3>

      <p>
        The visualization includes budgeted spending data for the
        <a
          class="text-link"
          href="https://controller.phila.gov/wp-content/uploads/2023/06/FY24-28-Five-Year-Plan-as-Adopted-FINAL.pdf"
          target="blank_"
        >
          <b>FY24 Adopted Budget</b></a
        >. Users can explore the adopted FY24 budget by comparing to previous
        budgets from fiscal years 2020 through 2023.
      </p>

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

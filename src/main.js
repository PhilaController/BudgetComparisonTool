import "core-js/stable";
import Vue from "vue";
import App from "@/App";
import vuetify from '@/plugins/vuetify' // path to vuetify export
import $ from "jquery"
import { descending } from 'd3-array';

Vue.config.productionTip = false;

// load and set the HTML template we are using
let audit_content = $(".audit-content");
audit_content.html(`<div id="app"></div>`);

function add_data_buttons() {
  /* Download the data */

  // spending button
  let spending_url = "https://raw.githubusercontent.com/PhiladelphiaController/BudgetComparisonTool/main/analysis/data/processed/budget-comparison-data.csv";
  let spending_btn = `<a id="downloadDataButton" href="${spending_url}" class="btn btn-primary btn-block btn-block">
            <i class="fas fa-download"></i>
            Download Budget Data
        </a>`;

  // Don't add more than once
  if ($("#downloadDataButton").length > 0) return;


  // add download data button and remove the report button
  $(".entry-header .btn").after(spending_btn).first().remove();
}


async function add_archive_button() {

  // Create a dropdown element and button
  let dropdown = $(`<div class="dropdown mt-2"></div>`);
  let button = $(`<button class="btn btn-primary btn-block dropdown-toggle" 
                    type="button" 
                    id="archiveButton" 
                    data-toggle="dropdown" 
                    aria-haspopup="true" 
                    aria-expanded="false">View Other Budgets</button>`);
  let dropdownMenu = $(
    `<div class="dropdown-menu w-100" 
          aria-labelledby="archiveButton"
          style="max-height: 300px; overflow-y: auto"></div>`
  );

  // Load the data
  let response = await fetch("https://raw.githubusercontent.com/PhilaController/BudgetComparisonTool/main/src/data/budgets.json");
  let data = await response.json();

  // Sort the data in descending order
  data = data.sort((a, b) => descending(a.fiscalYear, b.fiscalYear));

  // This budget
  let thisBudget = __TAG__;

  // Add each URL
  let baseURL = "https://controller.phila.gov/philadelphia-audits/";
  for (let i = 0; i < data.length; i++) {
    let item = data[i]
    let fy = item.fiscalYear.slice(2);
    let upperKind = item.kind.charAt(0).toUpperCase() + item.kind.slice(1);
    let tag = `FY${fy}-${upperKind}`

    // Skip the current report
    if (tag === thisBudget) continue;

    // Get the slug and label
    let slug = `the-${item.kind}-fy${fy}-budget`
    let label = `FY${fy} ${upperKind}`;

    // Otherwise, add the dropdown item
    dropdownMenu.append(
      `<a class="dropdown-item" style = "color: #212529;" href = "${baseURL}/${slug}">${label}</a>`
    );
  }
  dropdown.append(button);
  dropdown.append(dropdownMenu);

  // Don't add more than once
  if ($("#archiveButton").length > 0) return;

  // Add the dropdown button
  $(".entry-header .btn")
    .last()
    .after(dropdown);
}


// Add the buttons
add_data_buttons()
add_archive_button()

// add help message
if ($(".help-message").length == 0) {
  let helpMessage = `<p class='help-message mt-2'>
      Comments or feedback ? Please contact
      <a href="mailto:controller@phila.gov"> controller@phila.gov</a>.
  </p> `;
  $(".back-link").after(helpMessage);
}


// mount the app
new Vue({
  vuetify,
  render: h => h(App)
}).$mount("#app");


// When document is loaded --> turn off FA tracking
$(document).ready(function () {
  window.FontAwesome.config.observeMutations = false;
  window.FontAwesome.config.searchPseudoElements = false;
});
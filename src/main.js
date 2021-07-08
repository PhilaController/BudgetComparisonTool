import "core-js/stable";
import Vue from "vue";
import App from "@/App";
import router from "@/router";
import vuetify from '@/plugins/vuetify' // path to vuetify export


Vue.config.productionTip = false;

// load and set the HTML template we are using
let audit_content = $(".audit-content");
audit_content.html(`<div id="app"></div>`);

function add_data_buttons() {
  /* Download the data */

  // spending button
  let spending_url = "https://raw.githubusercontent.com/PhiladelphiaController/BudgetComparisonTool/main/analysis/data/processed/FYP2226-adopted-by-major-class.csv";
  let spending_btn = `<a href="${spending_url}" class="btn btn-primary btn-block btn-block">
            <i class="fas fa-download"></i>
            Download Budget Data
        </a>`;

  // add download data button and remove the report button
  $(".entry-header .btn").after(spending_btn).first().remove();
}


function add_archive_button() {
  let dropdown = $(`<div class="dropdown mt-2"></div>`);

  let button = $(`<button class="btn btn-primary btn-block dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
  View Past Budgets</button>`);

  let dropdownMenu = $(
    `<div class="dropdown-menu w-100" aria-labelledby="dropdownMenuButton"></div>`
  );

  let baseURL = "https://controller.phila.gov/philadelphia-audits/";
  let slugs = [
    "the-proposed-fy22-budget",

  ];
  let texts = ["FY22 Proposed"];

  for (let i = 0; i < slugs.length; i++) {
    dropdownMenu.append(
      `<a class="dropdown-item" href="${baseURL}/${slugs[i]}">${texts[i]}</a>`
    );
  }
  dropdown.append(button);
  dropdown.append(dropdownMenu);

  // add the dropdown button
  $(".entry-header .btn")
    .last()
    .after(dropdown);
}


// Add the buttons
add_data_buttons()
add_archive_button()

// add help message
let helpMessage = `<p class='help-message mt-2'>
  Comments or feedback? Please contact
  <a href="mailto:controller.policy@phila.gov">controller.policy@phila.gov</a>.
  </p>`;
$(".back-link").after(helpMessage);


// mount the app
new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");


// When document is loaded --> turn off FA tracking
$(document).ready(function () {
  window.FontAwesome.config.observeMutations = false;
  window.FontAwesome.config.searchPseudoElements = false;
});
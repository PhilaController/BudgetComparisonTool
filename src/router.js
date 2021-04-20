import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Guide from "@/views/Guide";

Vue.use(Router);

export default new Router({
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: "/",
      component: Home
    },
    {
      path: "/guide",
      component: Guide
    },
  ]
});

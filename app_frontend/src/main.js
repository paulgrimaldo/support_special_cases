import Vue from 'vue'
import App from './App'
import router from './router'
import TheNavBar from './components/TheNavBar'
import TheFooter from './components/TheFooter'
import AppButton from "./components/AppButton";
import SpecialCaseContainer from './components/SpecialCaseContainer'
import StudentDetail from './components/StudentDetail'
import ClassesSelector from './components/ClassesSelector'
import LoadingIndicator from "./components/LoadingIndicator";
import ProcessSummary from "./components/ProcessSummary";
import ToastMessage from "./components/ToastMessage";
import GroupsSelector from "./components/GroupsSelector";
import store from './store'

Vue.config.productionTip = false;
Vue.component('the-navbar', TheNavBar);
Vue.component('the-footer', TheFooter);
Vue.component('app-button', AppButton);
Vue.component('special-case-container', SpecialCaseContainer);
Vue.component('student-detail', StudentDetail);
Vue.component('classes-selector', ClassesSelector);
Vue.component('loading-indicator', LoadingIndicator);
Vue.component('process-summary', ProcessSummary);
Vue.component('toast-message', ToastMessage);
Vue.component('groups-selector', GroupsSelector);

new Vue({
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
});

Vue.directive('uppercase', {
  update(el) {
    el.value = el.value.toUpperCase()
  },
});

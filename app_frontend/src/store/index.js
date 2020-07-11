import Vue from 'vue'
import Vuex from 'vuex'
import student from './modules/student';
import classes from './modules/classes';
import groups from "./modules/groups";
import * as actions from './actions';
import * as mutations from './mutations';
import {state} from './state';

Vue.use(Vuex);

export default new Vuex.Store({
  state,
  actions,
  mutations,
  modules: {
    student,
    classes,
    groups,
  }
})

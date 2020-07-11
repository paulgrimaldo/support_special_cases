import {TEMPLATES} from "../../global";

const state = () => ({});

const getters = {
  classes: (state, getters, rootState) => {
    return rootState
      .studentCareerData
      .classes;
  }
};

const mutations = {};

const actions = {
  confirmGroupsSelection: ({dispatch}) => {
    const template = TEMPLATES.SENDING_SPECIAL_CASE_DATA;

    dispatch('setTemplate', template, {root: true});
    dispatch('generateDocumentation', null, {root: true});
  },
  cancelGroupsSelection: ({dispatch}) => {
    const template = TEMPLATES.CLASSES_SELECTOR;
    dispatch('setTemplate', template, {root: true})
  },
  updateClassGroup: ({state}, payload) => {
    const classData = payload.classData;
    const group = payload.group;

    if (group === "") {
      delete classData.group;

      return;
    }

    classData.group = group;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}

import {TEMPLATES} from "../../global";

export const state = () => ({
  classType: "none",
});

export const getters = {
  orderedClasses: (state, getters, rootState) => {
    const reversed = {};
    const original = rootState.studentCareerData.classes;

    Object.keys(original)
      .reverse()
      .forEach(function (key) {
        reversed[key] = original[key];
      });

    return reversed;
  },
  isInvalidClassType: (state) => {
    return state.classType === 'none';
  }
};

export const mutations = {
  setClassType: (state, {classType}) => {
    state.classType = classType;
  }
};

export const actions = {
  setClassType: ({commit}, classType) => {
    commit('setClassType', {classType})
  },
  updateClassType: ({commit, state}, classData) => {
    if (classData.type && classData.type === state.classType) {
      delete classData.type;

      return;
    }

    classData.type = state.classType;
  },
  confirmClassesSelection: ({dispatch}) => {
    const template = TEMPLATES.GROUPS_SELECTOR;
    dispatch('setTemplate', template, {root: true});
    dispatch('setClassType', 'none');
  },
  cancelClassesSelection: ({dispatch}) => {
    const template = TEMPLATES.STUDENT_DETAIL;
    dispatch('setTemplate', template, {root: true});
    dispatch('setClassType', 'none');
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}

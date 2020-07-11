import {TEMPLATES} from "../../global";

const state = () => ({
  student: {
    name: null,
    code: null,
    dni: null,
    phone: null
  },
  careerData: null
});

export const mutations = {
  setInitialCareer: (state, {initialCareer}) => {
    state.careerData = {
      ...initialCareer,
      idx: 0
    }
  },
  setSelectedCareer: (state, {career, careerIndex}) => {
    if (career != null) {
      state.careerData = {
        ...career,
        idx: careerIndex
      };
    }
  }
};

export const actions = {
  setInitialCareer: ({commit, rootState}) => {
    const initialCareer = rootState.careersData[0];
    commit('setInitialCareer', {initialCareer});
  },
  setSelectedCareer: ({commit, rootState}, key) => {
    const career = rootState.careersData.find(career => career.key === key);
    const careerIndex = rootState.careersData.indexOf(career);

    commit('setSelectedCareer', {career, careerIndex});
  },
  confirmStudentDetails: ({state, rootState, dispatch}) => {
    rootState.studentData = state.student;
    rootState.studentCareerData = state.careerData;

    const template = TEMPLATES.CLASSES_SELECTOR;
    dispatch('setTemplate', template, {root: true});
  }
};

export const getters = {
  getCareers: (state, getters, rootState) => {
    return rootState.careersData
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}

import {TEMPLATES} from "../global";

export const setCareers = (state, {careers}) => {
  state.careersData = careers;
};

export const setProcessSummary = (state, {processSummary}) => {
  state.processSummary = processSummary;
  state.template = TEMPLATES.PROCESS_SUMMARY;
};

export const setTemplate = (state, {template}) => {
  state.template = template;
};

export const resetApp = (state) => {
  state.template = TEMPLATES.STUDENT_DETAIL;
  state.studentData = null;
  state.studentCareerData = null;
  state.studentClassesData = null;
  state.careersData = null;
  state.processSummary = {
    title: null,
    summary: null,
    actionTitle: null,
    success: null,
  };
};

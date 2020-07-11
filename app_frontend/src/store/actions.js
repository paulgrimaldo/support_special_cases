import axios from 'axios';
import {saveAs} from "file-saver";

export const getCareers = ({commit}) => {
  axios
    .get(process.env.GET_CAREERS_API_URL)
    .then(response => commit('setCareers', {careers: response.data.careers}))
    .catch(error => {
      console.error(error);

      commit('setProcessSummary', {
        processSummary: {
          title: 'Ops ... 😰',
          summary: 'No pudimos cargar los datos desde el servidor, reinicia la aplicaci&oacuten por favor.',
          actionTitle: 'Reiniciar aplicaci&oacute;n',
          success: false
        }
      });

    });
};

export const generateDocumentation = ({commit, state}) => {
  const payload = {
    student: {
      ...state.studentData
    },
    career_data: {
      name: state.studentCareerData.name,
      director: state.studentCareerData.director,
      key: state.studentCareerData.key,
      classes: state.studentCareerData.classes
    }
  };
  axios
    .post(process.env.GENERATE_DOCUMENTATION_API_URL, payload, {
      responseType: "blob",
      headers: {"Access-Control-Allow-Origin": "*"}
    })
    .then(response => {
      const filename = decodeURI(response.headers['x-suggested-filename']);
      saveAs(response.data, filename);

      commit('setProcessSummary', {
        processSummary: {
          title: 'Documentos generados',
          summary: 'Ey ... ' + state.studentData.name + ' tus documentos han sido generados con &eacute;xito 😁⚡',
          actionTitle: 'Volver al inicio',
          success: true
        }
      });
    })
    .catch(error => {
      console.error(error);

      commit('setProcessSummary', {
        processSummary: {
          title: 'Ops ... 😰',
          summary: 'Ocurri&oacute; un error inesperado,Por favor vuelve atr&aacute;s e intenta de nuevo...',
          actionTitle: 'Volver al inicio',
          success: false
        }
      });

    });
};

export const setTemplate = ({commit}, template) => {
  commit('setTemplate', {template})
};

export const resetApp = ({commit, dispatch}) => {
  commit('resetApp');
  dispatch('getCareers');
};

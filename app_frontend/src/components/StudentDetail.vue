<template>
  <section class="row justify-content-center">
    <div class="col-lg-12 text-center">
      <h1>Datos del estudiante</h1>
    </div>
    <div class="col-sm-12 col-md-6 col-lg-6 col-xl-6 shadow-lg p-3 m-3 bg-white rounded">
      <div class="form-group">
        <label for="name">Nombres y apellidos</label>
        <input
          v-model="student.name"
          type="text"
          class="form-control"
          id="name"
          name="name"
          placeholder="p. ej. Paul Fernando Grimaldo Bravo"
        />
      </div>
      <div class="form-group">
        <label for="code">Registro Universitario</label>
        <input
          v-model="student.code"
          type="text"
          class="form-control"
          id="code"
          name="code"
          placeholder="p. ej. 214040801"
        />
      </div>
      <div class="form-group">
        <label for="ci">Carnet de identidad</label>
        <input
          v-model="student.dni"
          type="text"
          class="form-control"
          id="ci"
          name="ci"
          placeholder="p. ej. 9796898"
        />
      </div>
      <div class="form-group">
        <label for="phone_number">N&uacute;mero de celular</label>
        <div class="input-group">
          <div class="input-group-prepend">
            <div class="input-group-text">+591</div>
          </div>
          <input
            v-model="student.phone"
            type="tel"
            class="form-control"
            id="phone_number"
            name="phone_number"
            placeholder="p. ej. 69000850"
          />
        </div>
      </div>
      <div class="form-group">
        <label for="career">Carrera</label>
        <select
          v-model="careerData.key"
          class="form-control"
          id="career"
          required
          @change="setSelectedCareer($event.target.value)"
        >
          <option v-for="career in careers" :key="career.key" :value="career.key">{{career.name}}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="career_director">Director de carrera</label>
        <div class="row">
          <div class="col-lg-10 col-md-10 col-sm-10 col-10">
            <input
              :disabled="disableEditCareerDirector"
              v-model="careerData.director"
              type="text"
              class="form-control"
              id="career_director"
              name="career_director"
              placeholder="Ing. Modesto Franklin Calderon"
            />
          </div>
          <div class="col-lg-2 col-md-2 col-sm-2 col-2">
            <button
              id="btnEditCareerDirector"
              class="btn"
              @click="onClickEditCareerDirector"
              data-toggle="tooltip"
              data-placement="top"
              title="Editar director de carrera"
            >
              <i class="fas fa-edit"></i>
            </button>
          </div>
        </div>
      </div>
      <app-button @click="onConfirmStudentDetails" style="float: right;">
        Siguiente
        <i class="fas fa-arrow-right"></i>
      </app-button>
    </div>
    <toast-message
      :id="'student-detail-error'"
      :content="'Rellene los campos con sus datos para continuar'"
    ></toast-message>
  </section>
</template>

<script>
  import {mapActions, mapGetters, mapState} from "vuex";

  export default {
    data() {
      return {
        disableEditCareerDirector: true,
        showToastError: false
      };
    },
    computed: {
      ...mapState('student', ['student', 'careerData']),
      ...mapGetters('student', {careers: 'getCareers'})
    },
    methods: {
      ...mapActions('student', ['setInitialCareer', 'setSelectedCareer', 'confirmStudentDetails']),
      onClickEditCareerDirector: function () {
        this.disableEditCareerDirector = !this.disableEditCareerDirector;
      },
      onConfirmStudentDetails: function () {
        const isValidName = this.student.name !== null && this.student.name.trim() !== '';
        const isValidCode = this.student.code !== null && this.student.code.trim() !== '';
        const isValidDni = this.student.dni !== null && this.student.dni.trim() !== '';
        const isValidPhone = this.student.phone !== null && this.student.phone.trim() !== '';

        if (isValidName && isValidCode && isValidDni && isValidPhone) {
          this.confirmStudentDetails();
          return;
        }

        this.showStudentDetailsError();
      },
      showStudentDetailsError: function () {
        this.showToastError = true;
        setTimeout(() => $("#student-detail-error").toast("show"), 0);
      }
    },
    beforeMount() {
      this.setInitialCareer();
      $('[data-toggle="tooltip"]').tooltip();
      $(".toast").toast();
    }
  };
</script>

<style>
</style>

<template>
  <div class="row justify-content-center">
    <div class="col-lg-12">
      <div class="text-center">
        <h2>{{studentCareerData.name}}</h2>
        <small>❗❗Esta aplicaci&oacute;n no realiza la validaci&oacute;n de pre-requisitos (Por ahora 😁).</small>
      </div>
      <!-- Class type radio button -->
      <div class="row text-sm-left text-md-center text-lg-center mt-4 mb-4">
        <div class="col-lg-12">
          <div class="custom-control custom-radio custom-control-inline">
            <input
              @change="setClassType('approved')"
              type="radio"
              id="approvedRadio"
              name="classType"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="approvedRadio">Materias aprobadas</label>
            <div class="color-indicator-container approved mt-2 ml-1"></div>
          </div>
          <div class="custom-control custom-radio custom-control-inline">
            <input
              @change="setClassType('registered')"
              type="radio"
              id="registeredRadio"
              name="classType"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="registeredRadio">Materias inscritas</label>
            <div class="color-indicator-container registered mt-2 ml-1"></div>
          </div>
          <div class="custom-control custom-radio custom-control-inline">
            <input
              @change="setClassType('special_case')"
              type="radio"
              id="specialCaseRadio"
              name="classType"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="specialCaseRadio">Materias para caso especial</label>
            <div class="color-indicator-container special-case mt-2 ml-1"></div>
          </div>
        </div>
      </div>
      <!-- Classes cards -->
      <div class="container-fluid scrolling-wrapper">
        <div
          class="row flex-row flex-nowrap"
          v-for="(studentClasses, semesterKey) in orderedClasses"
          :key="semesterKey"
        >
          <div
            class="card ml-2 mt-2 text-center class-card"
            v-for="studentClass in studentClasses"
            :key="studentClass.initials"
            :id="studentClass.initials"
            :style="classesCardStyles[studentClass.type]"
            @click="onClickClass(studentClass)"
          >
            <div class="card-body">
              <h5 class="card-title class-title">{{studentClass.name}}</h5>
              <p class="card-text class-initials">{{studentClass.initials}}</p>
              <small v-if="studentClass.elective"><i>Electiva</i></small>
            </div>
          </div>
        </div>
      </div>
    </div>

    <template v-if="showToastError">
      <toast-message
        :id="'classes-selection-error'"
        :content="'Tienes que seleccionar tus materias (Aprobadas, Inscritas y Caso Especial)'"
        @clickCloseToast="showToastError = false"
      ></toast-message>
    </template>

    <app-button @click="cancelClassesSelection" class="mt-2">
      <i class="fas fa-arrow-left"></i>
      Atr&aacute;s
    </app-button>
    <app-button class="mt-2 ml-2" @click="onConfirmClassesSelection">
      Siguiente
      <i class="fas fa-arrow-right"></i>
    </app-button>
  </div>
</template>

<script>
  import {mapActions, mapGetters, mapState} from "vuex";

  export default {
    data() {
      return {
        showToastError: false,
        classesCardStyles: {
          none: {
            backgroundColor: "#ffffff",
            color: "#000000"
          },
          approved: {
            backgroundColor: "#FFFF00",
            color: "#000000"
          },
          registered: {
            backgroundColor: "#008000",
            color: "#000000"
          },
          special_case: {
            backgroundColor: "#FF0000",
            color: "#ffffff"
          }
        },
      };
    },
    computed: {
      ...mapState(['studentCareerData']),
      ...mapState('classes', ['classType']),
      ...mapGetters('classes', ['orderedClasses', 'isInvalidClassType'])
    },
    methods: {
      ...mapActions('classes', ['setClassType', 'updateClassType', 'confirmClassesSelection', 'cancelClassesSelection']),
      onClickClass: function (clickedClass) {
        if (this.isInvalidClassType) {
          this.showClassesSelectionError();
          return;
        }
        const classCard = $(`#${clickedClass.initials}`);
        const classCardStyle = this.getClassCardStyleFor(clickedClass);
        classCard.css(classCardStyle);

        this.updateClassType(clickedClass);
      },
      showClassesSelectionError: function () {
        this.showToastError = true;
        setTimeout(() => $("#classes-selection-error").toast("show"), 0);
      },
      getClassCardStyleFor: function (classData) {
        return classData.type && classData.type === this.classType
          ? this.classesCardStyles["none"]
          : this.classesCardStyles[this.classType];
      },
      onConfirmClassesSelection: function () {
        const isValidSpecialCase = this.validateClasses(
          semester => semester[1].find(klass => klass.type && klass.type === 'special_case') !== undefined
        );
        const isValidRegistered = this.validateClasses(
          semester => semester[1].find(klass => klass.type && klass.type === 'registered') !== undefined
        );
        const isValidApproved = this.validateClasses(
          semester => semester[1].find(klass => klass.type && klass.type === 'approved') !== undefined
        );
        if (isValidApproved && isValidRegistered && isValidSpecialCase) {
          this.confirmClassesSelection();
          return;
        }

        this.showClassesSelectionError();
      },
      validateClasses: function (predicate) {
        return Object.entries(this.orderedClasses).find(predicate) !== undefined;
      }
    },
    mounted() {
      $(".toast").toast();
    }
  };
</script>

<style scoped>
  .class-row::before,
  .class-row::after {
    content: "";
    flex: 1;
  }

  .class-title {
    font-size: 13px;
    height: 50px;
  }

  .class-initials {
    font-size: 12px;
  }

  .class-card {
    width: 9rem;
    max-height: 140px;
    cursor: pointer;
    -ms-flex: 0 9rem;
    flex: 0 0 9rem;
    max-width: 9rem;
  }

  .class-card:hover {
    transform: translateY(-5px);
  }

  .color-indicator-container {
    width: 10px;
    height: 10px;
    border-radius: 2px;
  }

  .color-indicator-container.approved {
    background-color: #FFFF00;
    color: #FFFF00;
  }

  .color-indicator-container.registered {
    background-color: #008000;
    color: #008000;
  }

  .color-indicator-container.special-case {
    background-color: #FF0000;
    color: #FF0000;
  }

  .scrolling-wrapper {
    overflow-x: auto;
  }
</style>

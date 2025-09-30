<template>
  <block-ab v-if="currentSpec" :title="currentSpec.name">
    <EntitiesImgScreen :instance="visibleSpec" :images="imageSpec" :separatePage="false" />
    <div class="ab__p">
      <p><b>Квалификация</b>: {{ currentSpec.qualification }}</p>
      <p><b>Срок обучения</b>: {{ currentSpec.period }}</p>
      <p><b>Форма обучения</b>: {{ currentSpec.formOfEducation }}</p>
    </div>
    <div class="slide__imgs" v-on:click="visibleSpec = !visibleSpec">
      <img
        v-if="currentSpec.imgdown"
        class="slide__img slide__img-down"
        alt="Slider-Image"
        loading="lazy"
        :src="currentSpec.imgdown" />
      <img
        v-if="currentSpec.imgc"
        class="slide__img"
        alt="Slider-Image"
        loading="lazy"
        :src="currentSpec.imgc" />
      <img
        v-if="currentSpec.imgup"
        class="slide__img slide__img-up"
        alt="Slider-Image"
        loading="lazy"
        :src="currentSpec.imgup" />
    </div>
    <div class="ab__p">
      <ul class="ab__list">
        <b>Основные виды деятельности выпускника:</b>
        <li v-for="(actv, actvIdx) of currentSpec.activities" :key="actvIdx">
          {{ actv }}
        </li>
      </ul>
    </div>
    <div class="ab__p" v-if="!currentSpec.careerMap">
      <ul class="ab__list">
        <b>Выпускник колледжа работает:</b>
        <li v-for="(job, jobIdx) of currentSpec.jobs" :key="jobIdx">{{ job }}</li>
      </ul>
    </div>
    <div v-if="currentSpec.careerMap" class="ab__p">
      <p><b>Карьерная карта</b>:</p>
      <div v-if="Array.isArray(currentSpec.careerMap)">
        <div v-for="map in currentSpec.careerMap" :key="map">
          <img
            :src="map"
            alt="Карьерная карта"
            @click="openFullImage(map)"
            class="small-career-map" />
        </div>
      </div>
      <div v-else>
        <img
          :src="currentSpec.careerMap"
          alt="Карьерная карта"
          @click="openFullImage(currentSpec.careerMap)"
          class="small-career-map" />
      </div>
    </div>

    <div class="full-image-modal" v-if="showFullImageModal" @click="showFullImageModal = false">
      <img :src="fullImage" alt="Полноразмерная карьерная карта" />
    </div>

    <div class="ab__p" v-if="currentSpec.plan != ''">
      <ul class="ab__list">
        <!-- экскурсионные услуги -->

        <li v-if="currentSpec.gos">
          <a class="ab__link" target="_blank" :href="currentSpec.gos">Гостиничные услуги, 2025г</a>
        </li>
        <li v-if="currentSpec.ekz">
          <a class="ab__link" target="_blank" :href="currentSpec.ekz"
            >Экскурсионные услуги, 2025г</a
          >
        </li>

        <li v-if="currentSpec.gos1">
          <a class="ab__link" target="_blank" :href="currentSpec.gos1"
            >Образовательная программа гостиничные услуги, 2025г</a
          >
        </li>
        <li v-if="currentSpec.ekz1">
          <a class="ab__link" target="_blank" :href="currentSpec.ekz1"
            >Образовательная программа экскурсионные услуги, 2025г</a
          >
        </li>

        <li v-if="currentSpec.gos2">
          <a class="ab__link" target="_blank" :href="currentSpec.gos2"
            >Учебный план гостиничные услуги</a
          >
        </li>
        <li v-if="currentSpec.ekz2">
          <a class="ab__link" target="_blank" :href="currentSpec.ekz2"
            >Учебный план экскурсионные услуги</a
          >
        </li>

        <li v-if="currentSpec.gos3">
          <a class="ab__link" target="_blank" :href="currentSpec.gos3"
            >Образовательная программа гостиничные услуги, 2025г</a
          >
        </li>
        <li v-if="currentSpec.ekz3">
          <a class="ab__link" target="_blank" :href="currentSpec.ekz3"
            >Образовательная программа экскурсионные услуги, 2025г</a
          >
        </li>

        <!--<b>Учебный план:</b>-->

        <li v-if="currentSpec.baza9">
          <a class="ab__link" target="_blank" :href="currentSpec.baza9"
            >Учебный план на базе основного общего образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.baza11">
          <a class="ab__link" target="_blank" :href="currentSpec.baza11"
            >Учебный план на базе среднего общего образования, 2025 г.</a
          >
        </li>

        <li v-if="currentSpec.plan2025web">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2025web"
            >Учебный план 2025 г</a
          >
        </li>
        <li v-if="currentSpec.z">
          <a class="ab__link" target="_blank" :href="currentSpec.z">Учебный план, 2025г</a>
        </li>
        <li v-if="currentSpec.zz">
          <a class="ab__link" target="_blank" :href="currentSpec.zz">Учебный план</a>
        </li>

        <li v-if="currentSpec.dev">
          <a class="ab__link" target="_blank" :href="currentSpec.dev">Учебный план (9 классов)</a>
        </li>
        <li v-if="currentSpec.odi">
          <a class="ab__link" target="_blank" :href="currentSpec.odi">Учебный план (11 классов)</a>
        </li>

        <li v-if="currentSpec.tov9">
          <a class="ab__link" target="_blank" :href="currentSpec.tov9">Товароведение (9 классов)</a>
        </li>
        <li v-if="currentSpec.tov11">
          <a class="ab__link" target="_blank" :href="currentSpec.tov11"
            >Товароведение (11 классов)</a
          >
        </li>
        <!-- 
        оБРАЗОВАТЕЛЬНАЯ ПРОГРАММА -->

        <li v-if="currentSpec.prof">
          <a class="ab__link" target="_blank" :href="currentSpec.prof"
            >Образовательная программа профессионалитета, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.prof2">
          <a class="ab__link" target="_blank" :href="currentSpec.prof2"
            >Образовательная программа профессионалитета, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.zzzz">
          <a class="ab__link" target="_blank" :href="currentSpec.zzzz"
            >Образовательная программа, 2025г</a
          >
        </li>

        <li v-if="currentSpec.programcoo">
          <a class="ab__link" target="_blank" :href="currentSpec.programcoo"
            >Образовательная программа COO</a
          >
        </li>
        <li v-if="currentSpec.programcoo2">
          <a class="ab__link" target="_blank" :href="currentSpec.programcoo2"
            >Образовательная программа ООО</a
          >
        </li>
        <li v-if="currentSpec.prof">
          <a class="ab__link" target="_blank" :href="currentSpec.prof"
            >Образовательная программа профессионалитета, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.prof2">
          <a class="ab__link" target="_blank" :href="currentSpec.prof2"
            >Образовательная программа профессионалитета, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.plan2025web2">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2025web2"
            >Образовательная программа, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.plan24">
          <a class="ab__link" target="_blank" :href="currentSpec.plan24"
            >Образовательная программа профессионалитета {{ currentSpec.nameprof }}</a
          >
        </li>
        <li v-if="currentSpec.plan244">
          <a class="ab__link" target="_blank" :href="currentSpec.plan244"
            >Образовательная программа профессионалитета {{ currentSpec.nameprof2 }}
          </a>
        </li>
        <li v-if="currentSpec.zzz">
          <a class="ab__link" target="_blank" :href="currentSpec.zzz">Образовательная программа</a>
        </li>
        <li v-if="currentSpec.zzz2">
          <a class="ab__link" target="_blank" :href="currentSpec.zzz">Образовательная программа</a>
        </li>

        <!-- OLD PLAN 2024 -->

        <li v-if="currentSpec.plan2024web">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2024web"
            >Учебный план по специальности 2024 г</a
          >
        </li>
        <li v-if="currentSpec.plan2024web2">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2024web2"
            >Учебный план по специальности 2024 г</a
          >
        </li>

        <!-- OLD PLAN 2023 -->

        <li v-if="currentSpec.planll">
          <a class="ab__link" target="_blank" :href="currentSpec.planll">Учебный план 2023 г</a>
        </li>
        <li v-if="currentSpec.planIX">
          <a class="ab__link" target="_blank" :href="currentSpec.planIX"
            >Учебный план на базе основного общего образования, 2023 г.</a
          >
        </li>
        <li v-if="currentSpec.planXI">
          <a class="ab__link" target="_blank" :href="currentSpec.planXI"
            >Учебный план на базе среднего общего образования, 2023 г.</a
          >
        </li>
      </ul>
    </div>
    <button class="back" @click="$router.go(-1)">Назад</button>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  data() {
    return {
      images: [],
      visibleSpec: false,
      fullImage: '',
      showFullImageModal: false,
    }
  },
  head() {
    return {
      title: this.currentSpec.name,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            this.currentSpec.name +
            'Квалификация ' +
            this.currentSpec.qualification +
            '. Основные виды деятельности выпускника: ',
        },
      ],
    }
  },
  async created() {
    if (this.specialties.length === 0) {
      const specs = JSON.parse(await loadDynamic('dynamic/specs/specs.json'))
      this.$store.commit('setSpecialties', specs)
    }
  },
  computed: {
    specCode() {
      return this.$route.params.code
    },
    specialties() {
      return this.$store.state.specialties
    },
    currentSpec() {
      return this.specialties.find((s) => s.code === this.specCode)
    },
    imageSpec() {
      return (this.images = [
        this.currentSpec.imgc,
        this.currentSpec.imgdown,
        this.currentSpec.imgup,
      ])
    },
    careerMap() {
      return this.currentSpec.careerMap
    },
    selectedCareerMap() {
      return this.currentSpec.selectedCareerMap
    },
  },
  methods: {
    openFullImage(image) {
      this.fullImage = image
      this.showFullImageModal = true
    },
  },
}
</script>

<style lang="scss" scoped>
.back {
  position: absolute;
  right: 16px;
  top: -50px;
  color: $bg-primary;
  background-color: $accent-color;
  padding: 12px 24px;
  border-radius: 12px;
  @include medium-media {
    position: fixed;
    top: 85px;
    right: 15px;
  }
}
.slide {
  background-color: #fff;
  padding: 70px 160px;
  height: 100%;
  width: 100%;
  position: relative;
  @include small-medium-media {
    padding: 24px 40px;
  }
  &__imgs {
    display: flex;
    position: absolute;
    right: 40px;
    top: 100px;
    cursor: pointer;
    @media screen and (max-width: 1680px) {
      position: static;
      padding: 20px;
    }
  }
  &__img {
    width: 300px;
    height: 300px;
    object-fit: cover;
    margin-right: 12px;
    flex: none;
    border-radius: 50%;
    &-down,
    &-up {
      width: 128px;
      height: 128px;
      @include high-media {
        // display: none;
      }
    }
    &-down {
      align-self: flex-end;
    }
    @include medium-media {
      width: 200px;
      height: 200px;
    }
    @include small-medium-media {
      width: 100px;
      height: 100px;
    }
  }
}
.small-career-map {
  cursor: pointer;
  width: 300px;
  height: auto;
}
.full-image-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000; /* Переносим модальное окно поверх других элементов */
}

.full-image-modal img {
  max-width: 90vw;
  max-height: 90vh;
}
</style>

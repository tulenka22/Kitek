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
    <div class="ab__p" v-if="currentSpec.jobs && currentSpec.jobs.length > 0">
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

        <li v-if="currentSpec.plan2026_ekz">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026_ekz">
            Учебный план (направленности - экскурсионные услуги), 2026 г.
          </a>
        </li>

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

        <!--ТУРИЗМ И ГОСТЕПРИИМСТВО (НАПРАВЛЕННОСТЬ: УСЛУГИ ПРЕДПРИЯТИЯ ПИТАНИЯ)-->

        <li v-if="currentSpec.plan2026_pit">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026_pit">
            Учебный план направленности "Услуги предприятия питания", 2026 г.
          </a>
        </li>

        <!--ТУРИЗМ И ГОСТЕПРИИМСТВО (НАПРАВЛЕННОСТЬ: ГОСТИНИЧНЫЕ УСЛУГИ)-->

        <li v-if="currentSpec.plan2026_gost">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026_gost">
            Учебный план направленности "Гостиничные услуги", 2026 г.
          </a>
        </li>
        <li v-if="currentSpec.tgg1">
          <a class="ab__link" target="_blank" :href="currentSpec.tgg1">
            Учебный план направленности "Гостиничные услуги", 2025 г.
          </a>
        </li>
        <li v-if="currentSpec.tgg3">
          <a class="ab__link" target="_blank" :href="currentSpec.tgg3">
            Образовательная программа направленности "Гостиничные услуги", 2025 г.
          </a>
        </li>
        <li v-if="currentSpec.tgg5">
          <a class="ab__link" target="_blank" :href="currentSpec.tgg5">
            Учебный план направленности "Гостиничные услуги", 2024 г.
          </a>
        </li>
        <li v-if="currentSpec.educationProgram2024">
          <a class="ab__link" target="_blank" :href="currentSpec.educationProgram2024">
            Образовательная программа направленности "Гостиничные услуги", 2024 г.
          </a>
        </li>


        <!--<b>Учебный план:</b>-->

        <li v-if="currentSpec.baza9">
          <a class="ab__link" target="_blank" :href="currentSpec.baza9"
            >Учебный план на базе основного общего образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.baza11">
          <a class="ab__link" target="_blank" :href="currentSpec.baza11"
            >Учебный план на базе среднего общего образования, 2025 г.
          </a>
        </li>

        <li v-if="currentSpec.plan2025web">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2025web"
            >Учебный план, 2025 г</a
          >
        </li>
        <li v-if="currentSpec.z">
          <a class="ab__link" target="_blank" :href="currentSpec.z">Учебный план, 2025 г.</a>
        </li>
        <li v-if="currentSpec.zz">
          <a class="ab__link" target="_blank" :href="currentSpec.zz">Учебный план.</a>
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
            >Образовательная программа, 2025г.</a
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
          <a class="ab__link" target="_blank" :href="currentSpec.planll">Учебный план, 2023 г.</a>
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

        <!-- ------------------------------------------------- -->
        <!-- ТД Коммерция -->
        <li v-if="currentSpec.td1">
          <a class="ab__link" target="_blank" :href="currentSpec.td1"
            >Учебный план (направленность - коммерция) на базе основного общего образования, 2025
            г.</a
          >
        </li>
        <li v-if="currentSpec.td2">
          <a class="ab__link" target="_blank" :href="currentSpec.td2"
            >Учебный план (направленность - коммерция) на базе среднего общего образования, 2025
            г.</a
          >
        </li>
        <li v-if="currentSpec.td3">
          <a class="ab__link" target="_blank" :href="currentSpec.td3"
            >Образовательная программа (направленность - коммерция) на базе основного общего
            образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.td4">
          <a class="ab__link" target="_blank" :href="currentSpec.td4"
            >Образовательная программа (направленность - коммерция) на базе среднего общего
            образования, 2025 г.</a
          >
        </li>

        <li v-if="currentSpec.td5">
          <a class="ab__link" target="_blank" :href="currentSpec.td5"
            >Учебный план (направленность - коммерция) на базе основного общего образования, 2024
            г.</a
          >
        </li>
        <li v-if="currentSpec.td6">
          <a class="ab__link" target="_blank" :href="currentSpec.td6"
            >Учебный план (направленность - коммерция) на базе среднего общего образования, 2024
            г.</a
          >
        </li>
        <li v-if="currentSpec.td7">
          <a class="ab__link" target="_blank" :href="currentSpec.td7"
            >Образовательная программа (направленность - коммерция) на базе основного общего
            образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.td8">
          <a class="ab__link" target="_blank" :href="currentSpec.td8"
            >Образовательная программа (направленность - коммерция) на базе среднего общего
            образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.td9">
          <a class="ab__link" target="_blank" :href="currentSpec.td9"
            >Учебный план (направленность - коммерция) на базе основного общего образования, 2023
            г.</a
          >
        </li>
        <li v-if="currentSpec.td10">
          <a class="ab__link" target="_blank" :href="currentSpec.td10"
            >Учебный план (направленность - коммерция) на базе среднего общего образования, 2023
            г.</a
          >
        </li>
        <!-- <li v-if="currentSpec.td11">
          <a class="ab__link" target="_blank" :href="currentSpec.td11"> </a>
        </li>
        <li v-if="currentSpec.td12">
          <a class="ab__link" target="_blank" :href="currentSpec.td12"> </a>
        </li>
        <li v-if="currentSpec.td13">
          <a class="ab__link" target="_blank" :href="currentSpec.td13"> </a>
        </li> -->

        <!-- ------------------------------------------------- -->
        <!-- ТД Товароведение -->
        <li v-if="currentSpec.tt1">
          <a class="ab__link" target="_blank" :href="currentSpec.tt1"
            >Учебный план (направленность - товароведение) на базе основного общего образования,
            2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tt2">
          <a class="ab__link" target="_blank" :href="currentSpec.tt2"
            >Учебный план (направленность - товароведение) на базе среднего общего образования, 2025
            г.</a
          >
        </li>
        <li v-if="currentSpec.tt3">
          <a class="ab__link" target="_blank" :href="currentSpec.tt3"
            >Образовательная программа (направленность - товароведение) на базе основного общего
            образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tt4">
          <a class="ab__link" target="_blank" :href="currentSpec.tt4"
            >Образовательная программа (направленность - товароведение) на базе среднего общего
            образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tt5">
          <a class="ab__link" target="_blank" :href="currentSpec.tt5"
            >Учебный план (направленность - товароведение) на базе основного общего образования,
            2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tt6">
          <a class="ab__link" target="_blank" :href="currentSpec.tt6"
            >Учебный план (направленность - товароведение) на базе среднего общего образования, 2024
            г.</a
          >
        </li>
        <li v-if="currentSpec.tt7">
          <a class="ab__link" target="_blank" :href="currentSpec.tt7"
            >Образовательная программа (направленность - товароведение) на базе основного общего
            образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tt8">
          <a class="ab__link" target="_blank" :href="currentSpec.tt8"
            >Образовательная программа (направленность - товароведение) на базе среднего общего
            образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tt9">
          <a class="ab__link" target="_blank" :href="currentSpec.tt9"
            >Учебный план (направленность - товароведение) на базе основного общего образования,
            2023 г.</a
          >
        </li>
        <li v-if="currentSpec.tt10">
          <a class="ab__link" target="_blank" :href="currentSpec.tt10"
            >Учебный план (направленность - товароведение) на базе среднего общего образования, 2023
            г.</a
          >
        </li>
        <li v-if="currentSpec.tt11">
          <a class="ab__link" target="_blank" :href="currentSpec.tt11"> </a>
        </li>
        <li v-if="currentSpec.tt">
          <a class="ab__link" target="_blank" :href="currentSpec.tt"> </a>
        </li>

        <!-- ------------------------------------------------- -->
        <!-- Повар кондитер -->

        <li v-if="currentSpec.plan20026">
          <a class="ab__link" target="_blank" :href="currentSpec.plan20026">
            Учебный план по профессии 43.01.09 Повар, кондитер, 2026 г.
          </a>
        </li>

        <li v-if="currentSpec.pk1">
          <a class="ab__link" target="_blank" :href="currentSpec.pk1">Учебный план, 2025 г.</a>
        </li>
        <li v-if="currentSpec.pk2">
          <a class="ab__link" target="_blank" :href="currentSpec.pk2"
            >Образовательная программа, 2025  г.</a
          >
        </li>
        <li v-if="currentSpec.pk3">
          <a class="ab__link" target="_blank" :href="currentSpec.pk3">Учебный план, 2024 г.</a>
        </li>
        <li v-if="currentSpec.pk4">
          <a class="ab__link" target="_blank" :href="currentSpec.pk4"
            >Образовательная программа, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.pk6">
          <a class="ab__link" target="_blank" :href="currentSpec.pk6"> </a>
        </li>
        <li v-if="currentSpec.pk7">
          <a class="ab__link" target="_blank" :href="currentSpec.pk7"> </a>
        </li>

        <!-- ------------------------------------------------- -->
        <!-- ПКД -->

        <li v-if="currentSpec.plan2026_9">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026_9">
            Учебный план на базе основного общего образования, 2026 г.
          </a>
        </li>
        <li v-if="currentSpec.plan2026_11">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026_11">
            Учебный план на базе среднего общего образования, 2026 г.
          </a>
        </li>

        <li v-if="currentSpec.pkd1">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd1"
            >Учебный план на базе основного общего образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd2">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd2"
            >Учебный план на базе среднего общего образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd3">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd3"
            >Образовательная программа на базе основного общего образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd4">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd4"
            >Образовательная программа на базе среднего общего образования, 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd5">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd5"
            >Учебный план на базе основного общего образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd6">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd6"
            >Учебный план на базе среднего общего образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd7">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd7"
            >Образовательная программа на базе основного общего образования, 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.pkd8">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd8"
            >Образовательная программа на базе среднего общего образования, 2024 г.</a
          >
        </li>
        <!-- <li v-if="currentSpec.pkd">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd"> </a>
        </li>
        <li v-if="currentSpec.pkd">
          <a class="ab__link" target="_blank" :href="currentSpec.pkd"> </a>
        </li> -->
        <!-- ------------------------------------------------- -->
        <!-- ТГ -->
        <li v-if="currentSpec.tg1">
          <a class="ab__link" target="_blank" :href="currentSpec.tg1"
            >Учебный план (направленность - гостиничные услуги), 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tg2">
          <a class="ab__link" target="_blank" :href="currentSpec.tg2"
            >Учебный план (направленность - экскурсионные услуги), 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tg3">
          <a class="ab__link" target="_blank" :href="currentSpec.tg3"
            >Образовательная программа (направленность - гостиничные услуги), 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tg4">
          <a class="ab__link" target="_blank" :href="currentSpec.tg4"
            >Образовательная программа (направленность - экскурсионные услуги), 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.tg5">
          <a class="ab__link" target="_blank" :href="currentSpec.tg5"
            >Учебный план (направленность - гостиничные услуги), 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tg6">
          <a class="ab__link" target="_blank" :href="currentSpec.tg6"
            >Учебный план (направленность - экскурсионные услуги), 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tg7">
          <a class="ab__link" target="_blank" :href="currentSpec.tg7"
            >Образовательная программа (направленность - гостиничные услуги), 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tg8">
          <a class="ab__link" target="_blank" :href="currentSpec.tg8"
            >Образовательная программа (направленность - экскурсионные услуги), 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.tg9">
          <a class="ab__link" target="_blank" :href="currentSpec.tg9"
            >Учебный план (направленность - гостиничные услуги), 2023 г.</a
          >
        </li>
        <li v-if="currentSpec.tg10">
          <a class="ab__link" target="_blank" :href="currentSpec.tg10"> </a>
        </li>
        <li v-if="currentSpec.tg">
          <a class="ab__link" target="_blank" :href="currentSpec.tg"> </a>
        </li>
        <!-- ------------------------------------------------- -->
        <!-- Юриспруденция -->

        <li v-if="currentSpec.plan2026">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026">
            Учебный план (очная форма обучения), 2026 г.
          </a>
        </li>
        <li v-if="currentSpec.plan2026z">
          <a class="ab__link" target="_blank" :href="currentSpec.plan2026z">
            Учебный план (заочная форма обучения), 2026 г.
          </a>
        </li>

        <li v-if="currentSpec.you1">
          <a class="ab__link" target="_blank" :href="currentSpec.you1"
            >Учебный план (очная форма обучения), 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.you2">
          <a class="ab__link" target="_blank" :href="currentSpec.you2"
            >Учебный план (заочная форма обучения), 2025 г.</a
          >
        </li>
        <li v-if="currentSpec.you3">
          <a class="ab__link" target="_blank" :href="currentSpec.you3"
            >Учебный план (очная форма обучения), 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.you4">
          <a class="ab__link" target="_blank" :href="currentSpec.you4"
            >Учебный план (заочная форма обучения), 2024 г.</a
          >
        </li>
        <li v-if="currentSpec.you5">
          <a class="ab__link" target="_blank" :href="currentSpec.you5"> </a>
        </li>
        <li v-if="currentSpec.you">
          <a class="ab__link" target="_blank" :href="currentSpec.you"> </a>
        </li>

        <!-- ------------------------------------------------- -->
        <!-- Моторист судовой -->
        <li v-if="currentSpec.mot1">
          <a class="ab__link" target="_blank" :href="currentSpec.mot1">Учебный план, 2025 г.</a>
        </li>
        <li v-if="currentSpec.mot2">
          <a class="ab__link" target="_blank" :href="currentSpec.mot2">Учебный план, 2024 г.</a>
        </li>
        <li v-if="currentSpec.mot3">
          <a class="ab__link" target="_blank" :href="currentSpec.mot3"> </a>
        </li>
        <li v-if="currentSpec.mot">
          <a class="ab__link" target="_blank" :href="currentSpec.mot"> </a>
        </li>
        <!-- ------------------------------------------------- -->
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

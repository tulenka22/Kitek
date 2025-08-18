<template>
  <block-ab title="Мастерские">
    <div class="block-zxc__right">
      <!-- документы -->
      <common-documents-list json-path="documents/workshop-links-1.json" />
      <!-- администрирование отеля, аттестация -->
      <common-documents-list json-path="documents/workshop-links-3.json" />
      <a class="ab__p ab__link" v-on:click="admatt = !admatt"></a>
      <div class="middle" v-for="emp in att" :key="emp.img" v-show="admatt">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b>Аттестат ЦПДЭ {{ emp.n }}</b>
        </p>
      </div>
      <!-- Свидетельства экспертов -->
      <a class="ab__p ab__link" v-on:click="admsvd = !admsvd"> Свидетельства экспертов </a>
      <div class="middle" v-for="emp in docadm" :key="emp.img" v-show="admsvd">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b> </b>
        </p>
      </div>
      <!-- Образовательные программы СПО -->
      <a class="ab__p ab__link" v-on:click="admspo = !admspo"> Образовательные программы СПО </a>
      <div v-show="admspo">
        <common-documents-list json-path="documents/workshop-adm-spo.json" />
      </div>
      <a class="ab__p ab__link" v-on:click="admprof = !admprof">
        Программы профессионального обучения
      </a>
      <div v-show="admprof">
        <common-documents-list json-path="documents/workshop-adm-prof.json" />
      </div>
      <p class="ab__p ab__link" v-on:click="dopprof = !dopprof">
        Дополнительные профессиональные программы повышения квалификации
      </p>
      <div v-show="dopprof">
        <common-documents-list json-path="documents/workshop-dop-prof.json" />
      </div>

      <common-documents-list json-path="documents/workshop-links-2.json" />
      <a class="ab__p ab__link" v-on:click="restsvd = !restsvd"> Свидетельства экспертов </a>
      <div class="middle" v-for="emp in docrest" :key="emp.img" v-show="restsvd">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b> </b>
        </p>
      </div>
      <a class="ab__p ab__link" v-on:click="restspo = !restspo"> Образовательные программы СПО </a>
      <div v-show="restspo">
        <common-documents-list json-path="documents/workshop-rest-spo.json" />
      </div>
      <a class="ab__p ab__link" v-on:click="restprof = !restprof">
        Программы профессионального обучения
      </a>
      <div v-show="restprof">
        <common-documents-list json-path="documents/workshop-rest-prof.json" />
      </div>
      <!-- ИТ-решения для бизнеса на платформе 1С Предприятие 8 и аттестаты-->
      <common-documents-list json-path="documents/workshop-links-4.json" />
      <a class="ab__p ab__link" v-on:click="itb1c = !itb1c"></a>
      <div class="middle" v-for="emp in attit" :key="emp.img" v-show="itb1c">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b>Аттестат ЦПДЭ {{ emp.n }}</b>
        </p>
      </div>
      <!-- программы -->
      <a class="ab__p ab__link" v-on:click="itb1cspo = !itb1cspo">
        Образовательные программы СПО
      </a>
      <!-- <div v-show="itb1cspo">
        <common-documents-list json-path="#" />
      </div> -->
      <a class="ab__p ab__link" v-on:click="itb1cprof = !itb1cprof">
        Программы профессионального обучения
      </a>
      <!-- <div v-show="itb1cprof">
        <common-documents-list json-path="#" />
      </div> -->
      <p class="ab__p ab__link" v-on:click="itb1cdopprof = !itb1cdopprof">
        Дополнительные профессиональные программы повышения квалификации
      </p>
      <!-- <div v-show="itb1cdopprof">
        <common-documents-list json-path="#" />
      </div> -->
      <!-- Программные решения для бизнеса и аттестаты-->
      <common-documents-list json-path="documents/workshop-links-5.json" />
      <a class="ab__p ab__link" v-on:click="prb = !prb"></a>
      <div class="middle" v-for="emp in attprb" :key="emp.img" v-show="prb">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b>Аттестат ЦПДЭ {{ emp.n }}</b>
        </p>
      </div>
      <!-- программы -->
      <a class="ab__p ab__link" v-on:click="prbspo = !prbspo"> Образовательные программы СПО </a>
      <!-- <div v-show="prbspo">
        <common-documents-list json-path="#" />
      </div> -->
      <a class="ab__p ab__link" v-on:click="prbprof = !prbprof">
        Программы профессионального обучения
      </a>
      <!-- <div v-show="prbprof">
        <common-documents-list json-path="#" />
      </div> -->
      <p class="ab__p ab__link" v-on:click="prbdopprof = !dopprof">
        Дополнительные профессиональные программы повышения квалификации
      </p>
      <!-- <div v-show="prbdopprof">
        <common-documents-list json-path="#" />
      </div> -->
      <!-- Поварское дело и аттестаты-->
      <common-documents-list json-path="documents/workshop-links-6.json" />
      <a class="ab__p ab__link" v-on:click="cook = !cook"></a>
      <div class="middle" v-for="emp in attcook" :key="emp.img" v-show="cook">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b>Аттестат ЦПДЭ {{ emp.n }}</b>
        </p>
      </div>
      <!-- программы -->
      <a class="ab__p ab__link" v-on:click="cookspo = !cookspo"> Образовательные программы СПО </a>
      <!-- <div v-show="cookspo">
        <common-documents-list json-path="#n" />
      </div> -->
      <a class="ab__p ab__link" v-on:click="cookprof = !cookprof">
        Программы профессионального обучения
      </a>
      <!-- <div v-show="cookprof">
        <common-documents-list json-path="#" />
      </div> -->
      <p class="ab__p ab__link" v-on:click="cookdopprof = !cookdopprof">
        Дополнительные профессиональные программы повышения квалификации
      </p>
      <!-- <div v-show="cookdopprof">
        <common-documents-list json-path="#" />
      </div> -->
      <!-- Предпринимательство и аттестаты-->
      <common-documents-list json-path="documents/workshop-links-7.json" />
      <a class="ab__p ab__link" v-on:click="entrep = !entrep"></a>
      <div class="middle" v-for="emp in attentrep" :key="emp.img" v-show="entrep">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b>Аттестат ЦПДЭ {{ emp.n }}</b>
        </p>
      </div>
      <!-- программы -->
      <a class="ab__p ab__link" v-on:click="entrepspo = !entrepspo">
        Образовательные программы СПО
      </a>
      <!-- <div v-show="entrepspo">
        <common-documents-list json-path="#" />
      </div> -->
      <a class="ab__p ab__link" v-on:click="entrepprof = !entrepprof">
        Программы профессионального обучения
      </a>
      <!-- <div v-show="entrepprof">
        <common-documents-list json-path="#" />
      </div> -->
      <p class="ab__p ab__link" v-on:click="entrepdopprof = !entrepdopprof">
        Дополнительные профессиональные программы повышения квалификации
      </p>
      <!-- <div v-show="entrepdopprof">
        <common-documents-list json-path="#" />
      </div> -->
      <!-- Веб-дизайн и разработка и аттестаты-->
      <common-documents-list json-path="documents/workshop-links-8.json" />
      <a class="ab__p ab__link" v-on:click="web = !web"></a>
      <div class="middle" v-for="emp in attweb" :key="emp.img" v-show="web">
        <img
          v-on:click="
            visible = !visible
            imgs = emp.img
          "
          class="img-single__preview"
          :src="'/img/projects/demoekzam-item/' + emp.img" />
        <p class="ab__p">
          <b>Аттестат ЦПДЭ {{ emp.n }}</b>
        </p>
      </div>
      <!-- программы -->
      <a class="ab__p ab__link" v-on:click="webspo = !webspo"> Образовательные программы СПО </a>
      <!-- <div v-show="webspo">
        <common-documents-list json-path="documents/workshop-adm-spo.json" />
      </div> -->
      <a class="ab__p ab__link" v-on:click="webprof = !webprof">
        Программы профессионального обучения
      </a>
      <!-- <div v-show="webprof">
        <common-documents-list json-path="documents/workshop-adm-prof.json" />
      </div> -->
      <p class="ab__p ab__link" v-on:click="webdopprof = !webdopprof">
        Дополнительные профессиональные программы повышения квалификации
      </p>
      <!-- <div v-show="webdopprof">
        <common-documents-list json-path="documents/workshop-dop-prof.json" />
      </div> -->

      <!-- Эксплуатация судов водного транспорта-->
      <common-documents-list json-path="documents/workshop-links-9.json" />

      <a href="/projects/workshop-events" class="ab__link ab__p"><b red>События</b></a>
      <a href="/projects/workshop-prof-school" class="ab__link ab__p document-list"
        ><b red>Профориентационная работа со школьниками</b></a
      >
    </div>
    <!-- кончился блок справа -->

    <!-- фото мастерских на странице -->
    <h2 class="ab__subtitle">
      &nbsp; В 2021 г. колледж стал участником федерального проекта «Молодые профессионалы»
      (Повышение конкурентоспособности профессионального образования)» национального проекта
      «Образование» в целях создания (обновления) материально-технической базы образовательных
      организаций, реализующих программы среднего профессионального образования.
    </h2>
    <p class="ab__p">
      &nbsp; В рамках реализации проекта в колледже были созданы 2 мастерские, оснащенные
      современной материально-технической базой по компетенциям "Ресторанный сервис" и
      "Администрирование отеля" для обеспечения практической подготовки обучающихся в соответствии с
      современными стандартами и передовыми технологиями.
    </p>
    <p class="ab__p"><b>Дата запуска мастерских:</b> 01 сентября 2022 г.</p>
    <p class="ab__p">
      &nbsp; Мастерская "Ресторанный сервис" используется для реализации образовательных программ по
      специальности 43.02.15 Поварское и кондитерское дело, профессии 43.01.09 Повар, кондитер,
      программ профессионального обучения, дополнительных профессиональных программ, программ
      профессиональной ориентации и т.п.
    </p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Ресторанный_сервис-1.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/Ресторанный_сервис-2.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Ресторанный_сервис-3.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/Ресторанный_сервис-4.webp" />
    </div>
    <p class="ab__p">
      &nbsp; Мастерская "Администрирование отеля" используется для реализации образовательных
      программ по специальностям 43.02.14 Гостиничное дело, 43.02.16 Туризм и гостеприимство,
      программ профессионального обучения, дополнительных профессиональных программ, программ
      профессиональной ориентации и т.п.
    </p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Администрирование_отеля-1.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/Администрирование_отеля-2.webp" />
    </div>
    <p class="ab__p">
      &nbsp; Оснащение мастерских соответствует современным международным стандартам в области
      ресторанного сервиса и гостеприимства, а обучающиеся получают дополнительные квалификации и
      осваивают новые востребованные компетенции.
    </p>
    <p class="ab__p">&nbsp; Мастерская "Веб-дизайн и разработка"</p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_1.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_3.webp" />
    </div>

    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_4.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_6.webp" />
    </div>

    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_8.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_Брендирование_1.webp" />
    </div>

    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/Веб_Брендирование_2.webp" />
    </div>

    <p class="ab__p">&nbsp; Мастерская "ИТ-решения для бизнеса на платформе 1С Предприятие"</p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ИТ-Брендирование_6.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ИТ-Фото_1.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ИТ-Фото_3.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ИТ-Фото_6.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ИТ-Фото_7.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ИТ-Фото_5.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ИТ-Фото_2.webp" />
    </div>

    <p class="ab__p">&nbsp; Мастерская "Поварское дело"</p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ПД-Брендирование_3.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ПД-Брендирование_1.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ПД-Брендирование_4.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ПД-Брендирование_8.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ПД-Брендирование_7.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ПД-Брендирование_6.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ПД-Брендирование_5.webp" />
    </div>

    <p class="ab__p">&nbsp; Мастерская "Программные решения для бизнеса"</p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ПРБ-Фото_1.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ПРБ-Фото_7.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ПРБ-Фото_5.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ПРБ-Фото_3.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ПРБ-Фото_12.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ПРБ-Фото_10.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ПРБ-Фото_9.webp" />
    </div>

    <p class="ab__p">&nbsp; Мастерская "Предпринимательство"</p>
    <div class="img-container">
      <img
        class="img-test__minimg"
        src="/img/projects/workshop/Предпринимательство_рабочее-место1.webp" />
      <img
        class="img-test__minimg"
        src="/img/projects/workshop/Предпринимательство_Брендирование_2.webp" />
    </div>

    <p class="ab__p">&nbsp; Мастерская "Эксплуатация судов водного транспорта"</p>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_6.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_27.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ЭСВТ-Фото_13.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ЭСВТ-Фото_12.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_9.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ЭСВТ-Фото_30.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ЭСВТ-Фото_21.webp" />
      <img class="img-test__minimg min_m" src="/img/projects/workshop/ЭСВТ-Фото_20.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_18.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_17.webp" />
    </div>
    <div class="img-container">
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_16.webp" />
      <img class="img-test__minimg" src="/img/projects/workshop/ЭСВТ-Фото_15.webp" />
    </div>
    <!-- видимость картинок при нажатии (аттестаты..) -->
    <div class="enlarged" v-show="visible">
      <icon-wrapper width="48" height="48" class="close" v-on:click="visible = false">
        <icon-close />
      </icon-wrapper>
      <img class="img-single__enlarged" :src="'/img/projects/demoekzam-item/' + imgs" />
    </div>

    <common-documents-list class="document-list" json-path="documents/workshop-links-1.json" />
    <common-documents-list class="document-list" json-path="documents/workshop-links-3.json" />

    <p class="ab__p document-list"><b>Аттестаты ЦПДЭ</b></p>
    <common-documents-list class="document-list" json-path="documents/demo-ekzam-adminAtt.json" />
    <p class="ab__p document-list">
      <b>Свидетельства экспертов</b>
      <a class="ab__p ab__link document-list" v-on:click="admspo = !admspo">
        Образовательные программы СПО
      </a>
    </p>
    <div v-show="admspo">
      <common-documents-list json-path="documents/workshop-adm-spo.json" />
    </div>
    <p class="ab__p document-list">
      <b>Программы профессионального обучения</b>
    </p>
    <common-documents-list class="document-list" json-path="documents/workshop-adm-prof.json" />
    <p class="ab__p document-list">
      <b>Дополнительные профессиональные программы повышения квалификации</b>
    </p>
    <common-documents-list class="document-list" json-path="documents/workshop-dop-prof.json" />
    <common-documents-list class="document-list" json-path="documents/workshop-links-2.json" />
    <p class="ab__p document-list">
      <b>Свидетельства экспертов</b>
      <a class="ab__p ab__link document-list" v-on:click="restspo = !restspo">
        Образовательные программы СПО
      </a>
    </p>
    <div v-show="restspo">
      <common-documents-list json-path="documents/workshop-rest-spo.json" />
    </div>
    <p class="ab__p document-list"></p>
    <p class="ab__p document-list">
      <b>Программы профессионального обучения</b>
    </p>
    <common-documents-list class="document-list" json-path="documents/workshop-rest-prof.json" />
    <a href="/projects/workshop-events" class="ab__link ab__p document-list"><b red>События</b></a>
    <a href="/projects/workshop-prof-school" class="ab__link ab__p document-list"
      ><b red>Профориентационная работа со школьниками</b></a
    >
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      att: [
        {
          img: 'Администрирование_отеля_1.png',
          n: '1',
        },
        {
          img: 'Администрирование_отеля_2.png',
          n: '2',
        },
        {
          img: 'Администрирование_отеля_3.png',
          n: '3',
        },
        {
          img: 'Администрирование_отеля_4.png',
          n: '4',
        },
      ],
      docadm: [
        {
          img: 'Свидетельство Козырева Елена Александровна.png',
          n: 'doc',
        },
        {
          img: 'Свидетельство Колиева Марина Александровна.png',
          n: 'doc',
        },
        {
          img: 'Свидетельство Максимова Елена Александровна.png',
          n: 'doc',
        },
        {
          img: 'Свидетельство Морозова Яна Станиславовна.png',
          n: 'doc',
        },
        {
          img: 'Свидетельство Юрьева Елена Георгиевна.png',
          n: 'doc',
        },
      ],
      attit: [
        {
          img: 'ИТ-решения_КИТЭК_1.1.png',
          n: '1',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.2.png',
          n: '2',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.3.png',
          n: '3',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.4.png',
          n: '4',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.5.png',
          n: '5',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.6.png',
          n: '6',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.8.png',
          n: '8',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.9.png',
          n: '9',
        },
        {
          img: 'ИТ-решения_КИТЭК_1.10.png',
          n: '10',
        },
      ],
      attprb: [
        {
          img: 'Прогр решения_КИТЭК_1.1.png',
          n: '1',
        },
        {
          img: 'Прогр решения_КИТЭК_1.2.png',
          n: '2',
        },
        {
          img: 'Прогр решения_КИТЭК_1.3.png',
          n: '3',
        },
        {
          img: 'Прогр решения_КИТЭК_1.4.png',
          n: '4',
        },
        {
          img: 'Прогр решения_КИТЭК_1.5.png',
          n: '5',
        },
        {
          img: 'Прогр решения_КИТЭК_1.6.png',
          n: '6',
        },
      ],
      attcook: [
        {
          img: 'Поварское дело_КИТЭК_1.1.png',
          n: '1',
        },
        {
          img: 'Поварское дело_КИТЭК_1.2.png',
          n: '2',
        },
        {
          img: 'Поварское дело_КИТЭК_1.3.png',
          n: '3',
        },
        {
          img: 'Поварское дело_КИТЭК_1.4.png',
          n: '4',
        },
        {
          img: 'Поварское дело_КИТЭК_1.5.png',
          n: '5',
        },
      ],
      attentrep: [
        {
          img: 'Предпринимательство_КИТЭК_1.1.png',
          n: '1',
        },
        {
          img: 'Предпринимательство_КИТЭК_1.2.png',
          n: '2',
        },
        {
          img: 'Предпринимательство_КИТЭК_1.3.png',
          n: '3',
        },
        {
          img: 'Предпринимательство_КИТЭК_1.4.png',
          n: '4',
        },
      ],
      attweb: [
        {
          img: 'Веб-технологии_КИТЭК_1.1.png',
          n: '1',
        },
        {
          img: 'Веб-технологии_КИТЭК_1.2.png',
          n: '2',
        },
        {
          img: 'Веб-технологии_КИТЭК_1.3.png',
          n: '3',
        },
        {
          img: 'Веб-технологии_КИТЭК_1.4.png',
          n: '4',
        },
        {
          img: 'Веб-технологии_КИТЭК_2.1.png',
          n: '5',
        },
      ],
      docrest: [
        {
          img: 'Свидетельство Севернюк И.А..jpg',
          n: '1',
        },
      ],
      visible: false,
      admsvd: false,
      admatt: false,
      itb1c: false,
      prb: false,
      cook: false,
      entrep: false,
      web: false,
      admprof: false,
      restsvd: false,
      restprof: false,
      dopprof: false,
      restspo: false,
      admspo: false,
      title: 'Мастерские',
      description:
        'Сведения о мастерских колледжа, оснащенных современным оборудованием в соответствии со стандартами Ворлдскиллс Россия.',
      imgs: '',
    }
  },
  head() {
    return {
      title: this.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.description,
        },
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.img-container {
  margin-top: 10px;
  display: flex;
  align-items: flex-start;
  @media screen and (max-width: 768px) {
    display: block;
    align-items: stretch;
  }
}
.ab__link {
  cursor: pointer;
  margin-top: 20px;
}
.img-test {
  margin: 10px;
  height: 600px;
  width: 980px;
  @media screen and (max-width: 768px) {
    height: 200px;
    width: 400px;
  }
  &__minimg {
    height: 300px;
    width: 490px;
    margin-right: 5px;
    margin-bottom: 5px;
  }
}
.min_m {
  object-fit: cover;
  width: 490px;
  height: 300px;
}
.middle {
  margin-left: auto;
  width: 200px;
  margin-right: auto;
}
.hidden {
  margin-top: 20px;
  cursor: pointer;
}
.enlarged {
  visibility: visible;
  top: 80px;
  left: 0px;
  position: fixed;
  width: 100vw;
  height: 100vh;
  background-color: rgba($color: #000000, $alpha: 0.5);
}
.close {
  color: #000;
  top: 60px;
  right: 50px;
  position: absolute;
  transition: $t height;
  transition: color $t;
  color: $icon-color;
  cursor: pointer;
  &:hover {
    color: $accent-color;
  }
}
</style>

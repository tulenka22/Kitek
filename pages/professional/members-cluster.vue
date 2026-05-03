<template>
  <block-ab title="Участники образовательного кластера «Союз+»">
    <div class="block-zxc__right">
      <a class="ab__link" href="/professional"> <b>О профессионалитете</b></a>
      <a class="ab__link" href="/professional/members-cluster">
        <b>Участники образовательного кластера «Союз+»</b></a
      >
      <a class="ab__link" href="/professional/news"> <b>Новости проекта</b></a>
      <a class="ab__link" href="/professional/careerMaps"> <b>Карьерные карты</b></a>
    </div>
    <p class="ab__p"><b>Колледжи-партнеры:</b></p>
    <swiper :options="swiperOptions">
      <swiper-slide class="ab__slide" v-for="(college, id) of college" :key="id">
        <a target="_blank" :href="college.url" class="ab__link">
          <img class="ab__img" :src="`/img/professional/college/${id}.png`" />
          <h2 class="ab__subtitle">
            <b>{{ college.text }}</b>
          </h2>
        </a>
      </swiper-slide>
    </swiper>
    <p class="ab__p"><b>Работодатели:</b></p>
    <swiper :options="swiperOptions" class="slider">
      <swiper-slide class="ab__slide" v-for="(companies, id) of companies" :key="id">
        <a target="_blank" :href="companies.url" class="ab__link">
          <img class="ab__img" :src="`/img/professional/companies/${id}.png`" />
          <h2 class="ab__subtitle">
            <b>{{ companies.text }}</b>
          </h2>
        </a>
      </swiper-slide>
    </swiper>
    <swiper :options="swiperOptionsMobile" class="slider__mobile">
      <swiper-slide class="ab__slide" v-for="(companies, id) of companies" :key="id">
        <a target="_blank" :href="companies.url" class="ab__link">
          <img class="ab__img" :src="`/img/professional/companies/${id}.png`" />
          <h2 class="ab__subtitle">
            <b>{{ companies.text }}</b>
          </h2>
        </a>
      </swiper-slide>
    </swiper>

    <div class="document-list">
      <a class="ab__link" href="/professional"> <b red>О профессионалитете</b></a>
      <a class="ab__link" href="/professional/members-cluster">
        <b red>Участники образовательного кластера «Союз+»</b></a
      >
      <a class="ab__link" href="/professional/news"> <b red>Новости проекта</b></a>
    </div>
    <a class="ab__link" href="https://япроф.рф/"
      ><img alt="Logo" target="_blank" src="/img/professional/ЛогоПроф2024.png" class="logo"
    /></a>
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      plan: null,
      college: [
        {
          url: 'https://omkkii.ru/',
          text: 'БПОУ Омской области «Омский колледж культуры и искусств»',
        },
        {
          url: 'http://otslx.ru/',
          text: 'БПОУ Омской области «Омский техникум строительства и лесного хозяйства»',
        },
        {
          url: 'https://omacademy.ru/',
          text: 'АНПОО "Омская академия экономики и предпринимательства"',
        },
      ],
      companies: [
        { url: 'https://kdlomsk.ru/', text: 'ООО «Коммерческая компания «Омск»' },
        { url: 'http://omsktest.ru/', text: 'ООО «Центр сертификации и экспертизы «ОМСК-ТЕСТ»' },
        { url: 'http://benefit-kpk.ru/', text: 'ООО «Консультационно-правовая компания «Бенефит»' },
        {
          url: 'https://nika.cronwell.com',
          text: 'Отель «Cronwell Park Ника» ИП Бомбин С.А',
        },
        {
          url: 'https://vk.com/club54761203?ysclid=lm4gez00jo476575976',
          text: 'ООО «Стройподряд»',
        },
        {
          url: 'hotel5060.ru',
          text: 'ООО "Компания "Топ Лайн"',
        },
        {
          url: 'https://krolik-omsk.ru/',
          text: 'ООО "Речной"',
        },
        {
          url: 'https://hutorokomsk.ru/',
          text: 'ИП Поротиков С.С.',
        },
        {
          url: 'https://proviant-omsk.ru/',
          text: 'ООО "Сибирский провиант"',
        },
        {
          url: 'https://sparomsk.ru/',
          text: 'ООО "Формат"',
        },
        {
          url: 'https://senkevich-omsk.ru/',
          text: 'ООО "СИБКОР-2"',
        },
      ],
      swiperOptions: {
        grabCursor: true,
        slidesPerView: 4,
        autoplay: {
          enabled: true,
          delay: 3000,
        },
      },
      swiperOptionsMobile: {
        grabCursor: true,
        slidesPerView: 2,
        autoplay: {
          enabled: true,
          delay: 3500,
        },
      },
    }
  },
}
</script>

<style scoped lang="scss">
.logo {
  position: absolute;
  width: 300px;
  height: 270px;
  right: 23%;
  top: 24px;
  opacity: 0.4;
  @include high-media() {
    width: 200px;
    height: 170px;
    right: 12px;
    top: 12px;
    opacity: 0.4;
  }
  @include small-media() {
    width: 150px;
    height: 130px;
    right: 10px;
    top: 10px;
    opacity: 0.3;
  }
}
.ab {
  &__img {
    width: 200px;
    height: 150px;
    margin-left: auto;
    margin-right: auto;
    object-fit: contain;
    margin-top: 24px;
  }
  &__slide {
    margin-right: 5px;
  }
  &__subtitle {
    text-align: center;
    max-width: 300px;
  }
}

.slider {
  @include small-media() {
    display: none;
  }
  &__mobile {
    display: none;
    @include small-media() {
      display: block;
    }
  }
}
</style>

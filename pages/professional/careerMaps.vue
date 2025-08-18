<template>
  <block-ab title="Карьерные карты">
    <div class="block-zxc__right">
      <a class="ab__link" href="/professional"> <b>О профессионалитете</b></a>
      <a class="ab__link" href="/professional/members-cluster">
        <b>Участники образовательного кластера «Союз+»</b></a
      >
      <a class="ab__link" href="/professional/news"> <b>Новости проекта</b></a>
      <a class="ab__link" href="/professional/careerMaps"> <b>Карьерные карты</b></a>
    </div>
    <swiper class="slider_committe" :options="swiperOptions">
      <swiper-slide>
        <img class="img-single__minimg" src="/img/spec/Карьерная карта 09.02.07 Программист.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img
          class="img-single__minimg"
          src="/img/spec/Карьерная карта 09.02.07 Разработчик веб.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img class="img-single__minimg" src="/img/spec/Карьерная карта 38.02.08 Коммерция.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img
          class="img-single__minimg"
          src="/img/spec/Карьерная карта 38.02.08 Товароведение.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img class="img-single__minimg" src="/img/spec/карьерная карта повор кондитер.png" />
      </swiper-slide>
      <swiper-slide>
        <img class="img-single__minimg" src="/img/spec/Карьерная карта 43.02.15 ПКД.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img
          class="img-single__minimg"
          src="/img/spec/Карьерная карта 43.02.16 Гостиничные услуги.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img
          class="img-single__minimg"
          src="/img/spec/Карьерная карта 43.02.16 Экскурсионные услуги.jpg" />
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
      swiperOptions: {
        grabCursor: true,
        slidesPerView: 1,
        autoplay: {
          enabled: true,
          delay: 10000,
        },
      },
      swiperOptionsMobile: {
        grabCursor: true,
        slidesPerView: 1,
        autoplay: {
          enabled: true,
          delay: 8000,
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
.img-single__minimg {
  height: auto;
  width: 1100px;
}
</style>

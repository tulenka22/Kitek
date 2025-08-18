<template>
  <div class="enlarged" v-show="visible">
    <div style="height: 100px; width: 100%"></div>
    <swiper :options="swiperOptions" class="slider">
      <swiper-slide>
        <img class="slider__img" alt="Slider-Image" src="/img/events/IMG_1838.webp" />
      </swiper-slide>
      <swiper-slide>
        <img class="slider__img" alt="Slider-Image" src="/img/events/IMG_1832.webp" />
      </swiper-slide>
      <swiper-slide>
        <img class="slider__img" alt="Slider-Image" src="/img/events/IMG_1827.webp" />
      </swiper-slide>
      <swiper-slide>
        <img class="slider__img" alt="Slider-Image" src="/img/events/IMG_1834.webp" />
      </swiper-slide>
    </swiper>
    <div class="slider__controls">
      <icon-wrapper width="48" height="48" class="slider__prev">
        <icon-circle-arrow />
      </icon-wrapper>
      <icon-wrapper width="48" height="48" class="slider__next">
        <icon-circle-arrow />
      </icon-wrapper>
      <icon-wrapper width="48" height="48" class="slider__close" v-on:click="visible = !visible">
        <icon-close />
      </icon-wrapper>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: true,
      swiperOptions: {
        grabCursor: true,
        navigation: {
          nextEl: '.slider__next',
          prevEl: '.slider__prev',
        },
      },
    }
  },
}
</script>

<style scoped lang="scss">
.enlarged {
  visibility: visible;
  top: 80px;
  left: 0px;
  position: fixed;
  z-index: 1200;
  width: 100vw;
  height: 100vh;
  background-color: rgba($color: #000000, $alpha: 0.5);
}
.slider {
  position: relative;
  height: 75vh;
  width: 60vw;
  background-color: #fff;
  transition: $t height;
  position: relative;
  &__controls {
    right: 24px;
    bottom: 24px;
    display: flex;
    align-items: center;
    z-index: 1300;
  }
  &__close {
    top: 100px;
    right: 50px;
    position: absolute;
  }
  &__next {
    top: 40vh;
    right: 50px;
    position: absolute;
    transform: rotate(-90deg);
  }
  &__prev {
    top: 40vh;
    left: 50px;
    position: absolute;
    margin-right: 12px;
    transform: rotate(90deg);
  }
  &__prev,
  &__close,
  &__next {
    transition: color $t;
    color: $icon-color;
    cursor: pointer;
    &:hover {
      color: $accent-color;
    }
  }
  &__img {
    width: 100%;
    height: 100%;
  }
}
</style>

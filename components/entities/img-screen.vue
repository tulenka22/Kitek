<template>
  <div class="perspective">
    <div class="enlarged" v-show="instance">
      <div style="height: 5vh; maxmax--width: 100%"></div>
      <swiper :options="swiperOptions" class="img">
        <swiper-slide v-for="emp in images" :key="emp">
          <img class="img__wind" alt="Slider-Image" :src="emp" loading="lazy" />
        </swiper-slide>
        <div class="img__pagination" slot="pagination" />
      </swiper>
      <div class="img__controls">
        <icon-wrapper width="48" height="48" class="img__prev">
          <icon-circle-arrow />
        </icon-wrapper>
        <icon-wrapper width="48" height="48" class="img__next">
          <icon-circle-arrow />
        </icon-wrapper>
        <icon-wrapper
          v-if="separatePage == true"
          width="48"
          height="48"
          class="img__close"
          v-on:click="$router.go(-1)">
          <icon-close />
        </icon-wrapper>
        <icon-wrapper
          v-if="separatePage == false"
          width="48"
          height="48"
          class="img__close"
          v-on:click="instance = !instance">
          <icon-close />
        </icon-wrapper>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EntitiesImgScreen',
  props: {
    instance: {
      type: Boolean,
    },
    separatePage: {
      type: Boolean,
    },
    images: {
      type: Array,
    },
  },
  data() {
    return {
      perspective: true,
      swiperOptions: {
        grabCursor: true,
        pagination: {
          el: '.img__pagination',
          bulletClass: 'swiper__bullet',
          bulletActiveClass: 'swiper__bullet-active',
        },
        grabCursor: true,
        navigation: {
          nextEl: '.img__next',
          prevEl: '.img__prev',
        },
      },
    }
  },
}
</script>

<style scoped lang="scss">
.perspective {
  margin-left: auto;
  margin-right: auto;
  background-color: #fff;
}
.enlarged {
  visibility: visible;
  top: 0px;
  left: 0px;
  position: fixed;
  z-index: 1200;
  width: 100%;
  height: 100%;
  background-color: rgba($color: #000000, $alpha: 0.8);
}
.img {
  top: 10%;
  max-height: 70vh;
  max-width: 60%;
  // background-color: #fff;
  transition: $t height;
  position: relative;
  @media screen and (max-width: 720px) {
    max-height: 70vh;
    max-width: 90%;
  }
  &__pagination {
    bottom: 10px;
    position: fixed;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1280;
    bottom: 16px !important;
  }
  &__controls {
    right: 24px;
    bottom: 24px;
    display: flex;
    align-items: center;
    z-index: 1300;
  }
  &__close {
    top: 140px;
    right: 50px;
    position: absolute;
  }
  &__next {
    top: 50vh;
    right: 50px;
    position: absolute;
    transform: rotate(-90deg);
  }
  &__prev {
    top: 50vh;
    left: 50px;
    position: absolute;
    margin-right: 12px;
    transform: rotate(90deg);
  }
  &__prev,
  &__close,
  &__next {
    z-index: 1300;
    transition: color $t;
    color: $icon-color;
    cursor: pointer;
    &:hover {
      color: $accent-color;
    }
  }
  &__wind {
    max-width: 100%;
    max-height: 50%;
    margin-left: auto;
    margin-right: auto;
    @media screen and (max-width: 720px) {
      max-height: 50%;
      max-width: 100%;
      margin-left: auto;
      margin-right: auto;
    }
    @media screen and (max-width: 320px) {
      max-height: 100%;
      max-width: 100%;
    }
  }
}
.swiper-slide {
  height: 140vh;
}
</style>

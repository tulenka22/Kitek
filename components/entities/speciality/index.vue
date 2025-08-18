<template>
  <div class="el" :class="{ 'el-active': state }">
    <header class="el__header" @click="polarState">
      <h2 class="el__h2">{{ instance.title }}</h2>
      <IconWrapper class="icon" width="40" height="40">
        <IconCircleArrow />
      </IconWrapper>
      <span class="el__underline" />
    </header>
    <div class="el__content">
      <div class="el__info">
        <p class="el__description">
          {{ instance.description }}
        </p>
        <p class="el__description__mobile">
          {{ instance.m_description }}
        </p>
        <CommonButton class="el__btn" @click="showSpecialities(true)">
          Выбрать специальность
        </CommonButton>
        <CommonButton class="el__btn__mobile" @click="showMobileSpecialities(true, instance.id)">
          Выбрать специальность
        </CommonButton>
      </div>
      <img :alt="`Специальность ${instance.title}`" class="el__img" :src="instance.icon" />
    </div>
    <EntitiesSpecialityList
      v-if="!isMobile"
      @state:update="(state) => (specState = state)"
      :specialties="instance.specialties"
      :instance="instance"
      :state="specState" />
  </div>
</template>

<script>
import { isMobile } from '~/core/utils/flags'
export default {
  name: 'CommonSpeciality',
  props: {
    instance: {
      type: Object,
    },
  },
  data() {
    return {
      state: false,
      specState: false,
      specStateMobile: false,
    }
  },
  mounted() {},
  methods: {
    polarState() {
      this.state = !this.state
    },
    showSpecialities(state) {
      this.specState = state
    },
    showMobileSpecialities(state, specId) {
      this.$emit('overlay-change-state', state, specId)
    },
  },
  computed: {
    isMobile() {
      return isMobile()
    },
  },
}
</script>

<style scoped lang="scss">
.el {
  position: relative;
  // box-shadow: $control-shadow;
  border-radius: $default-border-radius;
  border: 1px solid $border-color;
  overflow: hidden;
  &__header {
    transition: $t box-shadow 400ms;
    position: relative;
    z-index: 51;
    padding: 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: $bg-control;
    border-radius: $default-border-radius;
    cursor: pointer;
    @include medium-media {
      padding: 24px 16px;
    }
    &:hover {
      .icon {
        color: $accent-color;
      }
    }
  }
  &__h2 {
    @extend %tg-h2;
    @include medium-media {
      font-size: 18px;
      margin-right: 12px;
    }
    user-select: none;
  }
  &__underline {
    position: absolute;
    transition: $t width 200ms;
    left: 0;
    bottom: 0;
    width: 0;
    height: 3px;
    border-radius: 5px;
    background-color: rgba($accent-color, 0.6);
  }
  &__info {
    width: 100%;
  }
  &__content {
    will-change: opacity, max-height;
    transition: $t max-height, $t padding, $t height, $t opacity;
    // shit-color
    // background-color: $beige-color;
    padding: 0 80px;

    display: flex;
    justify-content: space-between;
    border-radius: 0 5px 0 5px;

    // Animation
    opacity: 0;
    max-height: 0;
    overflow: hidden;

    position: relative;

    @include medium-media {
      padding: 0 20px;
    }
  }
  &__description {
    @extend %tg-h3;
    max-width: 600px;
    &__mobile {
      @extend %tg-h3;
      font-size: 16px;
      line-height: 21px;
      letter-spacing: 1.5px;
      display: none;
    }
    @include medium-media {
      display: none;
      &__mobile {
        display: block;
      }
    }
  }
  &__btn {
    margin-top: 48px;
    padding: 24px 48px !important;
    &__mobile {
      display: none;
      font-size: 16px;
      padding: 12px;
      width: 100%;
      margin-top: 24px;
      @include medium-media {
        display: block;
      }
    }
    @include medium-media {
      display: none;
    }
  }
  &__img {
    height: 400px;
    width: 400px;
    margin-right: 100px;

    @keyframes circle-rotation {
      0% {
        transform: rotate(0deg) translate(0px, 0px);
      }
      50% {
        transform: rotate(3deg) translate(-8px, -10px);
      }
      100% {
        transform: rotate(-1deg) translate(1px, 1px);
      }
    }
    transform-origin: 50% 50%;
    animation: circle-rotation 10s ease-in-out infinite alternate;

    @include medium-media {
      // transform-origin: 0 0;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 220px;
      height: 220px;
      z-index: -1;
      opacity: 0.25;
      margin-right: 0;
      animation: none;
    }
  }
  &-active {
    .el {
      &__header {
        box-shadow: $special-shadow;
        .icon {
          transform: rotate(180deg);
          color: $accent-color;
        }
        .el__underline {
          width: 100%;
        }
      }
      &__content {
        max-height: 736px;
        padding: 100px 80px;
        @include medium-media {
          padding: 32px 20px;
          max-height: 400px;
        }
        opacity: 1;
      }
    }
  }
}
</style>

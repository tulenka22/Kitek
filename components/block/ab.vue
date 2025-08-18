<template>
  <div class="abstract-container">
    <div
      class="ab"
      :class="{
        textBackCollorBlack: isActiveTextBackCollorBlack,
        textBackCollorBrown: isActiveTextBackCollorBrown,
        textBackCollorBlue: isActiveTextBackCollorBlue,
        textBackCollorYellow: isActiveTextBackCollorYellow,
        textSizeMedium: isActiveTextSizeMedium,
        textSizeHigh: isActiveTextSizeHigh,
        hideImages: isActiveHideImages,
        blackWhiteImages: isActiveBWImages,
      }">
      <h1 class="ab__title">{{ title }}</h1>
      <div class="ab__content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlockAb',
  data() {
    return {
      isActiveTextSizeMedium: false,
      isActiveTextSizeHigh: false,
      isActiveTextBackCollorBlack: false,
      isActiveTextBackCollorBrown: false,
      isActiveTextBackCollorBlue: false,
      isActiveTextBackCollorYellow: false,
      isActiveHideImages: false,
      isActiveBWImages: false,
    }
  },
  props: {
    title: String,
  },
  mounted() {
    if (localStorage.getItem('isActiveBWImages')) {
      this.isActiveBWImages = true
    }

    if (localStorage.getItem('isActiveHideImages')) {
      this.isActiveHideImages = true
    }

    if (localStorage.getItem('isActiveTextBackCollorBlack')) {
      this.isActiveTextBackCollorBlack = true
    }

    if (localStorage.getItem('isActiveTextBackCollorYellow')) {
      this.isActiveTextBackCollorYellow = true
    }

    if (localStorage.getItem('isActiveTextBackCollorBlue')) {
      this.isActiveTextBackCollorBlue = true
    }

    if (localStorage.getItem('isActiveTextBackCollorBrown')) {
      this.isActiveTextBackCollorBrown = true
    }

    if (localStorage.getItem('isActiveTextSizeMedium')) {
      this.isActiveTextSizeMedium = true
    }

    if (localStorage.getItem('isActiveTextSizeHigh')) {
      this.isActiveTextSizeHigh = true
    }
  },
  watch: {
    isActiveTextSizeMedium(Boolean) {
      localStorage.isActiveTextSizeMedium = Boolean
    },
    isActiveTextSizeHigh(Boolean) {
      localStorage.isActiveTextSizeHigh = Boolean
    },
    isActiveTextBackCollorBlack(Boolean) {
      localStorage.isActiveTextBackCollorBlack = Boolean
    },
    isActiveTextBackCollorBrown(Boolean) {
      localStorage.isActiveTextBackCollorBrown = Boolean
    },
    isActiveTextBackCollorBlue(Boolean) {
      localStorage.isActiveTextBackCollorBlue = Boolean
    },
    isActiveTextBackCollorYellow(Boolean) {
      localStorage.isActiveTextBackCollorYellow = Boolean
    },
    isActiveHideImages(Boolean) {
      localStorage.isActiveHideImages = Boolean
    },
    isActiveBWImages(Boolean) {
      localStorage.isActiveBWImages = Boolean
    },
  },
}
</script>

<style lang="scss">
.ab {
  padding: 40px;
  background-color: $bg-control;
  box-shadow: $special-shadow;
  border-radius: 8px;
  &__title {
    @extend %tg-header;
    color: $primary-color;
    font-size: 26px;
    line-height: 28px;
    max-width: 1200px;
    @include medium-media() {
      font-size: 16px;
      line-height: 18px;
    }
  }
  &__subtitle {
    margin-top: 24px;
    @extend %tg-ab-subtitle;
    max-width: 900px;
    &:first-child {
      margin-top: 0;
    }
    @include medium-media() {
      font-size: 14px;
      line-height: 16px;
      margin-top: 12px;
    }
    &-center {
      font-size: 18px;
      text-align: center;
    }
  }
  &__content {
    position: relative;
    padding: 12px 4px;
    min-height: 100vh;
    @include medium-media() {
      padding: 16px 4px;
    }
  }
  &__p {
    margin-top: 12px;
    max-width: 1000px;
    text-align: justify;
    @extend %tg-ab-text;
    @include medium-media() {
      font-size: 14px;
    }
  }
  &__list {
    margin-top: 24px;
    max-width: 900px;
    > li {
      position: relative;
      margin-top: 8px;
      margin-left: 8px;
      @extend %tg-ab-text;
      &::before {
        content: '';
        position: absolute;
        display: block;
        width: 4px;
        height: 4px;
        left: -8px;
        background-color: $primary-text-color;
        border-radius: 50%;
        margin-right: 4px;
        margin-top: 4px;
        flex: none;
      }
    }
    &-number {
      margin-top: 24px;
      max-width: 900px;
      list-style-type: decimal;
      > li {
        margin-top: 8px;
        margin-left: 8px;
        @extend %tg-ab-text;
        &::before {
          background-color: $primary-text-color;
          margin-right: 4px;
        }
      }
    }
  }
  &__link {
    margin-top: 8px;
    display: block;
    text-decoration: underline;
    text-underline-offset: 2px;
    @include medium-media() {
      line-height: 16px;
      font-size: 14px;
    }
  }
  @include medium-media() {
    padding: 32px 16px 16px 16px;
  }
}
.a-table {
  border-spacing: 0;
  border-collapse: collapse;
  margin-top: 12px;

  &__cell {
    @include tg(12px, 500, 14px, 0.5px);
    padding: 12px;
    border: 1px solid rgb(209, 209, 209);
    text-align: justify;
    max-width: 400px;
    &-8 {
      padding: 8px;
    }
    &-head {
      @include tg(16px, 600, 18px, 0.5px);
      text-align: left;
    }
    &-center {
      text-align: center;
      font-weight: 600;
    }
    @include medium-media {
      text-overflow: ellipsis;
      overflow: hidden;
      padding: 4px;
      &-head {
        font-size: 14px;
      }
    }
  }
}
</style>

<style scoped lang="scss">
.abstract-container {
  padding: 32px;
  @include medium-media() {
    padding: 16px;
  }
}
</style>

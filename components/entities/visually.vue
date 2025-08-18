<template>
  <div class="visually-panel">
    <dt>Размер шрифта:</dt>
    <dd>
      <a
        class="visually-fontsize visually-fontsize-standart"
        :class="FontSizeNone"
        @click=";(isActiveTextSizeNone = !isActiveTextSizeNone), resetSize(), $router.go(0)">
        A</a
      >
      <a
        class="visually-fontsize visually-fontsize-medium"
        :class="FontSizeMedium"
        @click="
          ;(isActiveTextSizeMedium = !isActiveTextSizeMedium),
            (isActiveTextSizeHigh = false),
            $router.go(0)
        "
        >A</a
      >
      <a
        class="visually-fontsize visually-fontsize-large"
        :class="FontSizeHigh"
        @click="
          ;(isActiveTextSizeHigh = !isActiveTextSizeHigh),
            (isActiveTextSizeMedium = false),
            $router.go(0)
        "
        >A</a
      >
    </dd>
    <dt>Изображение:</dt>
    <dt>
      <label
        style="cursor: pointer"
        v-if="isActiveHideImages == false"
        @click=";(isActiveHideImages = true), $router.go(0)">
        <iconWrapper height="30" width="30" style="position: absolute; top: 5px">
          <IconImgStrikethrough />
        </iconWrapper>
      </label>
      <label
        style="cursor: pointer"
        v-if="isActiveHideImages == false && isActiveBWImages == false"
        @click=";(isActiveBWImages = true), $router.go(0)">
        <iconWrapper height="30" width="30" style="position: absolute; margin-left: 30px; top: 5px">
          <IconImgBW />
        </iconWrapper>
      </label>
      <label
        style="cursor: pointer"
        v-if="isActiveBWImages == true && isActiveHideImages == false"
        @click="CollorImages(), $router.go(0)">
        <iconWrapper height="30" width="30" style="position: absolute; margin-left: 30px; top: 5px">
          <IconImg />
        </iconWrapper>
      </label>
      <label
        style="cursor: pointer"
        v-if="isActiveHideImages == true"
        @click="activateImages(), $router.go(0)">
        <iconWrapper height="30" width="30" style="position: absolute; top: 5px">
          <IconImg />
        </iconWrapper>
      </label>
    </dt>
    <dt></dt>
    <dt v-if="isActiveHideImages == false"></dt>
    <dt>Цвета:</dt>
    <dd>
      <a
        class="visually-colors visually-colors-bonw"
        :class="BackCollorWhite"
        @click="resetCollor(), $router.go(0)"
        ><span>A</span></a
      >
      <a
        class="visually-colors visually-colors-wonb"
        :class="BackCollorBlack"
        @click=";(isActiveTextBackCollorBlack = !isActiveTextBackCollorBlack), $router.go(0)"
        ><span>A</span></a
      >
      <a
        class="visually-colors visually-colors-buonw"
        :class="BackCollorBlue"
        @click=";(isActiveTextBackCollorBlue = !isActiveTextBackCollorBlue), $router.go(0)"
        ><span>A</span></a
      >
      <a
        class="visually-colors visually-colors-yonw"
        :class="BackCollorYellow"
        @click=";(isActiveTextBackCollorYellow = !isActiveTextBackCollorYellow), $router.go(0)"
        ><span>A</span></a
      >
      <a
        class="visually-colors visually-colors-bronw"
        :class="BackCollorBrown"
        @click=";(isActiveTextBackCollorBrown = !isActiveTextBackCollorBrown), $router.go(0)"
        ><span>A</span></a
      >
    </dd>
    <dd>
      <a
        class="visually-colors visually-colors-bonw"
        @click=";(isActiveTextSizeNone = !isActiveTextSizeNone), resetStyle(), $router.go(0)"
        ><span>Сброс</span></a
      >
    </dd>
  </div>
</template>

<script>
import IconWrapper from '../IconWrapper.vue'

export default {
  data() {
    return {
      test: true,
      isActiveTextSizeMedium: false,
      isActiveTextSizeHigh: false,
      isActiveTextSizeNone: false,
      isActiveTextBackCollorNone: false,
      isActiveTextBackCollorBlack: false,
      isActiveTextBackCollorBrown: false,
      isActiveTextBackCollorBlue: false,
      isActiveTextBackCollorYellow: false,
      isActiveHideImages: false,
      isActiveBWImages: false,
      isActiveImages: false,
    }
  },
  computed: {
    FontSizeNone() {
      if (this.isActiveTextSizeNone == true) {
        return {
          'visually-fontsize-active': true,
        }
      }
      if (this.isActiveTextSizeNone == false) {
        if (this.isActiveTextSizeMedium == this.isActiveTextSizeHigh) {
          return {
            'visually-fontsize-active': true,
          }
        } else {
          localStorage.removeItem('isActiveTextSizeNone')
          return {
            'visually-fontsize-active': false,
          }
        }
      }
    },
    FontSizeMedium() {
      if (this.isActiveTextSizeMedium == true) {
        localStorage.removeItem('isActiveTextSizeHigh')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
    FontSizeHigh() {
      if (this.isActiveTextSizeHigh == true) {
        localStorage.removeItem('isActiveTextSizeMedium')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
    BackCollorBlack() {
      if (this.isActiveTextBackCollorBlack == true) {
        localStorage.removeItem('isActiveTextBackCollorBrown')
        localStorage.removeItem('isActiveTextBackCollorBlue')
        localStorage.removeItem('isActiveTextBackCollorYellow')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
    BackCollorBrown() {
      if (this.isActiveTextBackCollorBrown == true) {
        localStorage.removeItem('isActiveTextBackCollorBlack')
        localStorage.removeItem('isActiveTextBackCollorBlue')
        localStorage.removeItem('isActiveTextBackCollorYellow')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
    BackCollorBlue() {
      if (this.isActiveTextBackCollorBlue == true) {
        localStorage.removeItem('isActiveTextBackCollorBrown')
        localStorage.removeItem('isActiveTextBackCollorBlack')
        localStorage.removeItem('isActiveTextBackCollorYellow')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
    BackCollorYellow() {
      if (this.isActiveTextBackCollorYellow == true) {
        localStorage.removeItem('isActiveTextBackCollorBrown')
        localStorage.removeItem('isActiveTextBackCollorBlue')
        localStorage.removeItem('isActiveTextBackCollorBlack')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
    BackCollorWhite() {
      if (this.isActiveTextBackCollorNone == true) {
        localStorage.removeItem('isActiveTextBackCollorBrown')
        localStorage.removeItem('isActiveTextBackCollorBlue')
        localStorage.removeItem('isActiveTextBackCollorYellow')
        localStorage.removeItem('isActiveTextBackCollorBlack')
        return {
          'visually-fontsize-active': true,
        }
      } else {
        return {
          'visually-fontsize-active': false,
        }
      }
    },
  },
  methods: {
    resetStyle() {
      localStorage.removeItem('isActiveTextSizeMedium')
      localStorage.removeItem('isActiveTextSizeHigh')
      localStorage.removeItem('isActiveTextBackCollorBlack')
      localStorage.removeItem('isActiveTextBackCollorBrown')
      localStorage.removeItem('isActiveTextBackCollorBlue')
      localStorage.removeItem('isActiveTextBackCollorYellow')
      localStorage.removeItem('isActiveHideImages')
      localStorage.removeItem('isActiveBWImages')
      localStorage.removeItem('specialButton')
    },
    resetSize() {
      localStorage.removeItem('isActiveTextSizeMedium')
      localStorage.removeItem('isActiveTextSizeHigh')
    },
    resetCollor() {
      localStorage.removeItem('isActiveTextBackCollorBlack')
      localStorage.removeItem('isActiveTextBackCollorBrown')
      localStorage.removeItem('isActiveTextBackCollorBlue')
      localStorage.removeItem('isActiveTextBackCollorYellow')
    },
    activateImages() {
      localStorage.removeItem('isActiveHideImages')
    },
    CollorImages() {
      localStorage.removeItem('isActiveBWImages')
    },
  },
  mounted() {
    if (localStorage.getItem('isActiveTextSizeNone')) {
      localStorage.removeItem('isActiveTextSizeMedium')
      localStorage.removeItem('isActiveTextSizeHigh')
    }
    if (localStorage.getItem('isActiveTextSizeHigh')) {
      localStorage.removeItem('isActiveTextSizeMedium')
      this.isActiveTextSizeHigh = true
    }
    if (localStorage.getItem('isActiveTextSizeMedium')) {
      localStorage.removeItem('isActiveTextSizeHigh')
      this.isActiveTextSizeMedium = true
    }
    if (localStorage.getItem('isActiveTextBackCollorBlack')) {
      this.isActiveTextBackCollorBlack = true
    }
    if (localStorage.getItem('isActiveTextBackCollorBrown')) {
      this.isActiveTextBackCollorBrown = true
    }
    if (localStorage.getItem('isActiveTextBackCollorBlue')) {
      this.isActiveTextBackCollorBlue = true
    }
    if (localStorage.getItem('isActiveTextBackCollorYellow')) {
      this.isActiveTextBackCollorYellow = true
    }
    if (localStorage.getItem('isActiveHideImages')) {
      this.isActiveHideImages = true
    }
    if (localStorage.getItem('isActiveBWImages')) {
      this.isActiveBWImages = true
    }
  },
  watch: {
    specialButton(Boolean) {
      localStorage.specialButton = Boolean
    },
    isActiveTextSizeNone(Boolean) {
      localStorage.isActiveTextSizeNone = Boolean
    },
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
  components: { IconWrapper },
}
</script>

<style lang="scss">
.hideImages {
  > * img {
    visibility: hidden !important;
    display: none !important;
  }
}
.blackWhiteImages {
  > * img {
    filter: grayscale(100%) !important;
  }
}

.textBackCollorBlack {
  background-color: #202020 !important;
  color: white !important;
  > * * {
    color: white !important;
    background-color: #202020 !important;
  }
}
.textBackCollorBrown {
  background-color: #4b0000 !important;
  color: #00af09 !important;
  > * * {
    color: #00af09 !important;
    background-color: #4b0000 !important;
  }
}
.textBackCollorBlue {
  background-color: #8ce8ff !important;
  color: #202020 !important;
  > * * {
    color: #202020 !important;
    background-color: #8ce8ff !important;
  }
}
.textBackCollorYellow {
  background-color: #feffd9 !important;
  color: #202020 !important;
  > * * {
    color: #202020 !important;
    background-color: #feffd9 !important;
  }
}
.textSizeMedium {
  > * * {
    font-size: 1.1em !important;
    line-height: normal !important;
  }
  > .ab__title {
    font-size: 2em !important;
  }
}
.textSizeHigh {
  > * * {
    font-size: 1.3em !important;
    letter-spacing: normal !important;
    line-height: 1.3em !important;
    max-width: 100%;
  }

  > .ab__title {
    font-size: 3em !important;
  }
}
</style>
<!-- !local style! -->
<style scoped lang="scss">
.visually {
  &-turn {
    &-off {
      margin-left: 60px;
    }
  }
  &-panel {
    // display: none;
    // position: absolute;
    height: 40px;
    top: 0;
    width: 100%;

    margin: 0;

    background: #f9f9f9;
    border-bottom: 1px solid #808080;

    font-size: 18px;
    line-height: 1.6;
    text-align: center;
    text-shadow: 0 1px 1px #fff;
    @include medium-media {
      display: none !important;
    }
    & dl {
      display: inline-block;
      margin: 0;
    }
    & dd {
      display: inline-block;
      margin: 0 5px;
    }
    & dt {
      display: inline-block;
      margin: 0 0px 0 25px;
      color: #444;
    }
    > input {
      width: 18px;
      height: 18px;
    }
  }
  &-fontsize {
    cursor: pointer;
    padding: 0 0.25em;
    margin: 0 2px;
    border: 1px solid transparent;
    text-decoration: none !important;
    &-standart {
      font-size: 14px !important;
    }
    &-medium {
      font-size: 18px !important;
    }
    &-large {
      font-size: 24px !important;
    }
    &-active {
      border: 1px solid #777;
      border-radius: 4px;
      background: #ccc;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) inset;
    }
  }
  &-colors {
    border: 1px solid transparent;
    padding: 5px 0;
    text-decoration: none !important;
    &-bonw {
      > span {
        cursor: pointer;
        color: #000 !important;
        background: #fff;
      }
    }
    &-buonw {
      > span {
        cursor: pointer;
        color: #202020 !important;
        background: #8ce8ff;
      }
    }
    &-yonw {
      > span {
        cursor: pointer;
        color: #202020 !important;
        background: #feffd9;
      }
    }
    &-bronw {
      > span {
        cursor: pointer;
        color: rgb(0, 156, 39) !important;
        background: #920000;
      }
    }
    &-wonb {
      > span {
        cursor: pointer;
        color: #fff !important;
        background: #000;
      }
    }
    &-active {
      border: 1px solid #777;
      border-radius: 4px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) inset;
    }
    > span {
      padding: 0 5px;
      margin: 0 2px;
      font-size: 120%;
      border-radius: 4px;
    }
  }
}
</style>

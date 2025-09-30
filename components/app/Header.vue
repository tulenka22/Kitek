<template>
  <div class="header__wrapper" @mouseleave="linkOut">
    <EntitiesVisually v-show="specialButton" />
    <header
      class="header"
      :class="{
        'header-shadow-hide': hamburgerState,
        textBackCollorBlack: isActiveTextBackCollorBlack,
        textBackCollorBrown: isActiveTextBackCollorBrown,
        textBackCollorBlue: isActiveTextBackCollorBlue,
        textBackCollorYellow: isActiveTextBackCollorYellow,
        textSizeMedium: isActiveTextSizeMedium,
        textSizeHigh: isActiveTextSizeHigh,
      }">
      <nuxt-link to="/" class="header__logo">
        <img src="/logo.webp" alt="Logotype KITEK" />
      </nuxt-link>
      <h1 class="header__title">БПОУ «КИТЭК»</h1>
      <div class="header__links">
        <nav class="header__nav header__nav-up" @mouseenter="linkOut">
          <nuxt-link to="/" class="header__link">Главная</nuxt-link>
          <nuxt-link to="/specialties" class="header__link">Специальности</nuxt-link>
          <nuxt-link to="/professional" class="header__link">Профессионалитет</nuxt-link>
          <nuxt-link to="/gordostkitek" class="header__link">Гордость КИТЭК</nuxt-link>
          <nuxt-link to="/spo85" class="header__link">85 лет системе СПО</nuxt-link>
          <!-- <nuxt-link to="/professional" class="header__link"
            ><img alt="Logo" src="/img/professional/ЛогоПроф2024.png" class="logo_prof"
          /></nuxt-link> -->
          <nuxt-link to="/umo" class="header__link">УМО</nuxt-link>
          <nuxt-link to="/search" class="header__link">Поиск</nuxt-link>
        </nav>
        <div class="header__separator header__separator-horizontal" />
        <nav class="header__nav header__nav-custom">
          <nuxt-link
            :to="link.url"
            v-for="(link, idx) of links"
            :key="idx"
            @mouseenter.native="linkEnter($event, link, idx)"
            class="custom-link header__link"
            :class="{
              'custom-link-active': currentNavComp === link.component && navState,
            }">
            {{ link.title }}
          </nuxt-link>
        </nav>
      </div>
      <div class="header__separator header__separator-vertical" />
      <div class="hamburger">
        <IconWrapper width="32" height="32" @click="hamburgerState = !hamburgerState">
          <IconHamburger :active="hamburgerState" />
        </IconWrapper>
      </div>
      <div class="contacts">
        <div class="contacts__row">
          <noindex>
            <div class="contacts__text">
              <p>Приемная директора: 68-07-73</p>
              <p>Приемная комиссия: 68-07-66</p>
              <p>E-mail: post@tradeconomy.omskportal.ru</p>
              <p>E-mail: tradeconomy@mail.ru</p>
            </div>
          </noindex>
          <a
            v-if="specialButton == false"
            class="specialButton"
            title="Версия сайта для слабовидящих"
            @click="specialButton = !specialButton">
            <IconWrapper width="24" height="24" class="icon contacts__eye">
              <IconEye />
            </IconWrapper>
          </a>
          <a
            v-if="specialButton == true"
            class="specialButton"
            title="Версия сайта для слабовидящих"
            @click="specialButtonDisable(), $router.go(0)">
            <IconWrapper width="24" height="24" class="icon contacts__eye">
              <IconEye />
            </IconWrapper>
          </a>
        </div>
        <div class="contacts__row">
          <div class="contacts__row contacts__socials">
            <a href="https://vk.com/omsktec" target="_blank" class="icon contacts__social">
              <IconWrapper width="24" height="24">
                <IconVK />
              </IconWrapper>
            </a>
            <a
              href="https://ok.ru/group/53402328629468"
              target="_blank"
              class="icon contacts__social">
              <IconWrapper width="24" height="24">
                <IconOK />
              </IconWrapper>
            </a>
            <!-- <a href="https://t.me/omskkitec" target="_blank" class="icon contacts__social">
              <IconWrapper width="24" height="24">
                <IconTelegram />
              </IconWrapper>
            </a> -->
            <a href="http://re-works.ru" target="_blank" class="icon contacts__social">
              <IconWrapper width="24" height="24">
                <IconRework />
              </IconWrapper>
            </a>
          </div>
          <nuxt-link to="/search">
            <IconWrapper width="24" height="24" class="icon">
              <IconSearch />
            </IconWrapper>
          </nuxt-link>
        </div>
      </div>
    </header>
    <div class="nav-categories" ref="navCategories" :class="{ 'nav-categories-active': navState }">
      <!-- linkOut saver -->
      <span />
      <component v-if="currentNavComp" :is="`Navdrop${currentNavComp}`" />
    </div>
    <div class="overlay" :class="{ 'overlay-active': hamburgerState }">
      <div class="overlay__content">
        <nuxt-link @click.native="hamburgerState = false" to="/" class="flat">
          <h2 class="flat__title">Главная</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
        <nuxt-link @click.native="hamburgerState = false" to="/specialties" class="flat">
          <h2 class="flat__title">Специальности</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
        <nuxt-link @click.native="hamburgerState = false" to="/professional" class="flat">
          <h2 class="flat__title">Профессионалитет</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
        <nuxt-link @click.native="hamburgerState = false" to="/gordostkitek" class="flat">
          <h2 class="flat__title">Гордость КИТЭК</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
        <nuxt-link @click.native="hamburgerState = false" to="/spo85" class="flat">
          <h2 class="flat__title">85 лет системе СПО</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
        <nuxt-link @click.native="hamburgerState = false" to="/umo" class="flat">
          <h2 class="flat__title">УМО</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
        <!-- <nuxt-link @click.native="hamburgerState = false" to="/" class="flat">
          <h2 class="flat__title">Дополнительное образование</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link> -->
        <!-- v-for links -->
        <nuxt-link
          :to="link.url"
          class="flat"
          v-for="(link, idx) of links"
          :key="idx"
          @click.native="hamburgerState = false">
          <h2 class="flat__title">{{ link.title }}</h2>
          <span />
          <IconWrapper height="24" width="24" class="flat__icon">
            <IconArrowDown />
          </IconWrapper>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
/**
 * @typedef DropLink
 * @property {string} url
 * @property {string} title
 * @property {string} component
 */
export default {
  name: 'AppHeader',
  data() {
    return {
      isActiveTextSizeMedium: false,
      isActiveTextSizeHigh: false,
      isActiveTextBackCollorBlack: false,
      isActiveTextBackCollorBrown: false,
      isActiveTextBackCollorBlue: false,
      isActiveTextBackCollorYellow: false,
      specialButton: false,
      // Nav
      navState: false,
      currentNavComp: null,

      /**
       * @type {DropLink[]}
       */
      links: [
        {
          url: '/organization/organization-menu',
          title: 'Сведения об образовательной организации',
          component: 'Organization',
        },
        {
          url: '/projects/projects-menu',
          title: 'Проекты',
          component: 'Projects',
        },
        {
          url: '/enrolle/enrolle-menu',
          title: 'Абитуриенту',
          component: 'Enrolle',
        },
        {
          url: '/student/student-menu',
          title: 'Студенту',
          component: 'Student',
        },
        {
          url: '/student/parents',
          title: 'Родителю',
          component: '',
        },
        {
          url: '/teacher/teacher-menu',
          title: 'Преподавателю',
          component: 'Teacher',
        },
      ],

      // mobile
      hamburgerState: false,
    }
  },
  methods: {
    /**
     * @param {MouseEvent} event
     * @param {DropLink | null} element
     * @param {number} idx
     */
    linkEnter(event, element, idx) {
      const { component } = element
      const windowWidth = window.innerWidth
      this.currentNavComp = component

      const { target } = event
      const { left } = target.getBoundingClientRect()

      // Используется для получения clientWidth после обновления <component :is/>
      this.$nextTick().then(() => {
        const clientWidth = this.navCategories.clientWidth

        // Получаем сколько px осталось для вмещения блока
        const permissible = windowWidth - left

        // Получаем N px сколько не помещается в экран
        const offsetLeft = clientWidth - permissible

        // Корректируем `left` |
        // Если допустимое блок может быть помещён т.е. имеет достаточное кол-во px
        // Чтобы не вылезать за пределы страницы
        // 24px -> Padding-left
        const correctedLeft = permissible < clientWidth ? left - (offsetLeft + 24) : left

        this.navState = true

        setTimeout(() => this.setLeftPosition(`${correctedLeft}px`), 100)
      })
    },
    linkOut() {
      this.navState = false
    },
    setLeftPosition(pos) {
      this.navCategories.style.left = pos
    },
    specialButtonDisable() {
      localStorage.removeItem('specialButton')
    },
  },
  computed: {
    /**
     * @returns {HTMLDivElement | undefined}
     */
    navCategories() {
      return this.$refs.navCategories
    },
  },
  mounted() {
    if (localStorage.getItem('specialButton')) {
      this.specialButton = true
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
    if (localStorage.getItem('isActiveTextSizeMedium')) {
      this.isActiveTextSizeMedium = true
    }

    if (localStorage.getItem('isActiveTextSizeHigh')) {
      this.isActiveTextSizeHigh = true
    }
  },
  watch: {
    specialButton(Boolean) {
      localStorage.specialButton = Boolean
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
  },
}
</script>

<style scoped lang="scss">
@import '~/assets/common';
.header {
  &__wrapper {
    position: sticky;
    top: 0;
    z-index: 10000;
    width: 100%;
    background-color: #ffffff;
    opacity: 0.97;
  }

  transition: $t box-shadow;

  padding: 16px 24px;
  display: flex;
  align-items: center;
  box-shadow: $nav-shadow;
  position: relative;
  z-index: 999;
  @include medium-media {
    padding: 8px 12px;
  }
  &-shadow-hide {
    box-shadow: none;
  }
  &__logo {
    width: 80px;
    height: 80px;
    margin-right: 48px;
    display: block;

    @include high-media {
      margin-right: 24px;
    }
    @include medium-media {
      width: 64px;
      height: 64px;
      margin-right: 0;
    }
    flex: none;

    > img {
      width: 99%;
      height: 99%;
      object-fit: contain;
    }
  }
  &__separator {
    background-color: $grey-color;
    &-vertical {
      height: 80px;
      width: 2px;
      margin: 0 12px 0 48px;
      @include high-media {
        margin-left: 24px;
      }
    }
    &-horizontal {
      height: 2px;
      width: 100%;
      margin: 10px 0;
    }
    @include medium-media {
      display: none;
    }
  }
  &__links {
    width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    @include medium-media {
      display: none;
    }
  }
  &__link {
    color: $primary-text-color;
    @extend %tg-navbar;
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    @include high-media {
      font-size: 12px;
    }
    @include medium-media {
      font-size: 20px;
    }
  }
  &__nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    @include medium-media {
      display: none;
    }
  }
  &__title {
    display: none;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
    font-size: 21px;
    font-weight: 500;
    line-height: 25px;
    @include medium-media {
      display: flex;
    }
  }
}

.contacts {
  flex: none;
  &__text {
    > p {
      margin-top: 4px;
      &:first-child {
        margin-top: 0;
      }
      @include tg(12px);
    }
    margin: 0 36px 12px 0;
  }
  &__row {
    display: flex;
  }
  &__social {
    &:nth-child(even) {
      margin: 0 12px;
    }
  }
  &__socials {
    flex-grow: 1;
  }
  @include medium-media {
    display: none;
  }
}

.custom-link {
  cursor: pointer;
  position: relative;
  &::after {
    content: '';
    transition: $t width;
    width: 0%;
    position: absolute;
    left: 0;
    bottom: -3px;
    height: 2px;
    background-color: $accent-color;
  }
  &-active {
    &::after {
      width: 100%;
    }
  }
}

.nav-categories {
  transition: $t left, $t opacity;

  position: absolute;
  // Где 120px -> Header-Height
  top: 118px + 4px + 20px;
  left: 24px;
  opacity: 0;
  pointer-events: none;
  box-shadow: $nav-drop-shadow;
  border-radius: 3px;
  background-color: $bg-control;
  &-active {
    pointer-events: all;
    opacity: 1;
  }
  > span {
    position: absolute;
    top: -8px;
    width: 100%;
    height: 8px;
    background-color: transparent;
    display: block;
    z-index: 10000;
  }
}

.hamburger {
  display: none;
  cursor: pointer;
  @include medium-media {
    display: block;
  }
}

.overlay {
  transition: $t opacity, $t left;
  position: fixed;
  bottom: 0;
  left: 100%;
  right: 0;
  top: 0;
  background-color: #ffffff;
  height: auto;
  width: 100%;
  pointer-events: none;
  opacity: 0;
  &__content {
    // position: relative;
    padding: 118px 12px 0 12px;
    height: 100%;
    // z-index: -1;
    overflow-y: auto;
    @include scrollbar;
  }
  &-active {
    left: 0;
    pointer-events: all;
    opacity: 1;
  }
}

.flat {
  padding: 20px 6px;
  border-bottom: 1px solid $border-color;
  display: flex;
  align-items: center;
  width: 100%;
  position: relative;
  &__title {
    font-family: Roboto;
    font-size: 16px;
    font-weight: 400;
    line-height: 19px;
  }
  &__icon {
    color: $nav-link;
    transform: rotate(-90deg);
  }
  > span {
    width: 48px;
    flex-grow: 1;
  }
}
.logo_prof {
  width: 80px;
  height: 75px;
}
</style>

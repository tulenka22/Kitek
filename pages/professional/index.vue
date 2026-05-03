<template>
  <block-ab title="Профессионалитет">
    <div class="docs-fab" @click="toggleDocs" :class="{ 'docs-fab--active': showDocs }">
      <span class="docs-fab__icon">📄</span>
      <div class="docs-fab__menu" v-if="showDocs">
        <!-- Ссылки из правого блока -->
        <a class="docs-fab__link" href="/professional">
          <span class="link-icon"></span> О профессионалитете
        </a>
        <a class="docs-fab__link" href="/professional/members-cluster">
          <span class="link-icon"></span> Участники образовательного кластера «Союз+»
        </a>
        <a class="docs-fab__link" href="/professional/news">
          <span class="link-icon"></span> Новости проекта
        </a>
        <a class="docs-fab__link" href="/professional/careerMaps">
          <span class="link-icon"></span> Карьерные карты
        </a>
      </div>
    </div>
    <!-- Видео без изменений, только добавлен контейнер с новыми стилями -->
    <div class="video-container">
      <video class="ab__video" controls>
        <source src="/video/profgoriz.mp4" type="video/mp4" />
      </video>

      <video class="ab__video vertical" controls>
        <source src="/video/profvertical.mp4" type="video/mp4" />
      </video>
    </div>

    <p class="ab__p">
      Профессионалитет — это образовательная программа в колледжах, которая позволит тебе стать
      высококвалифицированным специалистом на ведущем предприятии твоего региона
    </p>
    <h2 class="ab__subtitle">Для кого создана программа?</h2>
    <p class="ab__p">Для выпускников 9-11 классов</p>
    <ul class="ab__list">
      <li>Актуальная рабочая профессия – в короткий срок</li>
      <li>Учеба по-новому – с упором на практику и IT</li>
      <li>Современные мастерские и высокотехнологичное оборудование</li>
      <li>Стажировки и трудоустройство в ведущие отраслевые компании страны</li>
      <li>Компетентные преподаватели с практическим опытом</li>
      <li>Программы обучения, разработанные совместно с работодателями</li>
    </ul>
    <p class="ab__p">
      Профессионалитет меняет не только программы обучения студентов колледжей, но и привлекает
      работодателей к образовательному процессу. Министерство просвещения РФ дает предприятиям
      возможность формировать программы под свои запросы, быть соучредителем процесса образования и,
      таким образом, самим участвовать в подготовке кадров.
    </p>
    <h2 class="ab__subtitle">Образовательный кластер «Союз+» в отрасли «Туризм и сфера услуг»</h2>
    <p class="ab__p">
      Программа «Профессионалитет» предлагает обучение по множеству интересных и разнообразных
      специальностей.
    </p>
    <p class="ab__p">
      Если ты любишь путешествовать, общаться с людьми, готовить вкусные десерты или не
      представляешь жизнь без качественного сервиса — эта отрасль для тебя!
    </p>
    <p class="ab__p">
      Здесь можно получить профессии в сфере туризма, гостиничного бизнеса, кондитерского искусства
      и многих других.
    </p>
    <p class="ab__p">
      Поступай в кластеры «Профессионалитета», чтобы найти занятие по душе и получить востребованную
      специальность!
    </p>
    <ul class="ab__list spec-li">
      <p class="ab__p">
        <b red
          >Специальности/профессии реализуемые в рамках федерального проекта «Профессионалитет»:</b
        >
      </p>
      <li v-if="fpSpecialties.length">
        <ul>
          <li v-for="spec of fpSpecialties" :key="spec.id">
            <nuxt-link
              v-if="
                spec.name != '40.02.01 ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ' &&
                spec.name != '43.02.14 ГОСТИНИЧНОЕ ДЕЛО'
              "
              class="ab__link"
              :to="`/specialties/${spec.code}`">
              {{ spec.name }}
            </nuxt-link>
          </li>
        </ul>
      </li>
    </ul>
    <h2 class="ab__subtitle">Участники образовательного кластера «Союз+»</h2>
    <p class="ab__p">Колледжи-партнеры:</p>
    <ul class="ab__list">
      <li>
        <a href="https://omkkii.ru/" class="ab__link"
          >БПОУ Омской области «Омский колледж культуры и искусств»</a
        >
      </li>
      <li>
        <a href="http://otslx.ru/" class="ab__link"
          >БПОУ Омской области «Омский техникум строительства и лесного хозяйства»</a
        >
      </li>
      <li>
        <a href="https://omacademy.ru/" class="ab__link"
          >АНПОО "Омская академия экономики и предпринимательства"</a
        >
      </li>
    </ul>
    <p class="ab__p">Работодатели:</p>
    <ul class="ab__list">
      <li><a href="https://kdlomsk.ru/" class="ab__link">ООО «Коммерческая компания «Омск»</a></li>
      <li>
        <a href="http://omsktest.ru/" class="ab__link"
          >ООО «Центр сертификации и экспертизы «ОМСК-ТЕСТ»</a
        >
      </li>
      <li>
        <a href="http://benefit-kpk.ru/" class="ab__link"
          >ООО «Консультационно-правовая компания «Бенефит»</a
        >
      </li>
      <li>
        <a href="https://nika.cronwell.com" class="ab__link"
          >Отель «Cronwell Park Ника» ИП Бомбин С.А</a
        >
      </li>
      <li>
        <a href="https://vk.com/club54761203?ysclid=lm4gez00jo476575976" class="ab__link"
          >ООО «Стройподряд»</a
        >
      </li>
      <br /><br /><br />

      <li>
        <a href="/data/programa-d-s/РГ_КС_КИТЭК-2025.pdf" class="ab__link"
          >Состав рабочей группы Координационного совета</a
        >
      </li>
      <li>
        <a
          href="/data/programa-d-s/Программа_популяризации_2024_Омская_область.pdf"
          class="ab__link"
          >Программа популяризации федерального проекта «Профессионалитет» в Омской области</a
        >
      </li>
      <li>
        <a
          href="/data/programa-d-s/_№Р_23_4792_от_08_12_2023_Распоряжение_Об_определении_ответственного.pdf"
          class="ab__link"
          >Распоряжение о назначении ответственного за реализацию региональной программы
          популяризации федерального проекта «Профессионалитет» на территории Омской области</a
        >
      </li>
      <li>
        <a
          href="/data/programa-d-s/План_проведения_мероприятий_программы_популяризации_федерального.pdf"
          class="ab__link"
          >План проведения мероприятий программы популяризации федерального проекта
          «Профессионалитет» образовательного кластера «Союз+» по отрасли «Туризм и сфера услуг»</a
        >
      </li>
      <li>
        <a
          href="/data/programa-d-s/Информационный_план_мероприятий_программы_популяризации_федерального.pdf"
          class="ab__link"
          >Информационный план мероприятий программы популяризации федерального проекта
          «Профессионалитет» образовательного кластера «Союз+»</a
        >
      </li>
      <li>
        <a href="/data/programa-d-s/Положение_об_УК_КИТЭК.pdf" class="ab__link"
          >Положение об Управляющей компании образовательно кластера среднего профессионального
          образования «Союз+»</a
        >
      </li>
      <li>
        <a href="/data/programa-d-s/Положение_об_НПК_с_подписями.pdf" class="ab__link"
          >Положение о проведении научно-практической конференции студентов и преподавателей</a
        >
      </li>
      <br />
      <li>
        <a href="/data/programa-d-s/otechobespechenii.pdf" class="ab__link"
          >О техническом обеспечении</a
        >
      </li>
    </ul>
    <h2 class="ab__subtitle">Полезные ссылки ФП "Профессионалитет"</h2>
    <div class="contacts__row">
      <div class="contacts__row contacts__socials">
        <a href="https://vk.com/public212649371" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconVK />
          </IconWrapper>
        </a>
        <a href="https://xn--n1abdr5c.xn--p1ai/" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconProfessional />
          </IconWrapper>
        </a>
      </div>
    </div>
    <div class="document-list">
      <a class="ab__link" href="/professional"> <b red>О профессионалитете</b></a>
      <a class="ab__link" href="/professional/members-cluster">
        <b red>Участники образовательного кластера «Союз+»</b>
      </a>
      <a class="ab__link" href="/professional/news"> <b red>Новости проекта</b></a>
      <a class="ab__link" href="/professional/careerMaps"> <b red>Карьерные карты</b></a>
    </div>

    <a class="ab__link" href="https://япроф.рф/">
      <img alt="Logo" target="_blank" src="/img/professional/ЛогоПроф2024.png" class="logo" />
    </a>
  </block-ab>
</template>

<script>
import Block from '~/components/app/Block.vue'
import { loadDynamic } from '~/core/helpers/file'
export default {
  components: { Block },
  data() {
    return {
      showDocs: false,
      plan: null,
      swiperOptions: {
        grabCursor: true,
        autoplay: {
          enabled: true,
          delay: 5000,
        },
      },
      title: 'Приёмная комиссия',
      description: '...', // ваше описание
      jsonPath: 'dynamic/rating/plan.json',
      table_plan: false,
      table: false,
      advantage: false,
    }
  },
  methods: {
    toggleDocs() {
      this.showDocs = !this.showDocs
    },
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
  async created() {
    try {
      this.plan = JSON.parse(await loadDynamic(this.jsonPath))
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
  computed: {
    specialties() {
      return this.$store.state.specialties
    },
    fpSpecialties() {
      return this.specialties.filter((s) => s.group === 'ФП')
    },
    otherSpecialties() {
      return this.specialties.filter((s) => s.group !== 'ФП')
    },
  },
}
</script>

<style scoped lang="scss">
// Все исходные стили остаются без изменений, добавляем только несколько новых снизу

.block-zxc__right {
  margin-left: 5px;
}
.video-container {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
  align-items: stretch;
  max-width: 600px;
}
.ab__video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
}
@media (max-width: 768px) {
  .video-container {
    grid-template-columns: 1fr;
  }
  .ab__video:first-child {
    aspect-ratio: 16 / 9;
  }
  .ab__video.vertical {
    aspect-ratio: 9 / 16;
    max-height: 500px;
  }
}
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
    object-fit: contain;
    margin-top: 24px;
  }
  &__sites {
    position: absolute;
    right: 24px;
    top: 24px;
    display: block;
  }
}
.slider_committe {
  margin: 0px;
  margin-top: 24px;
  max-width: 1000px;
}
.contacts {
  flex: none;
  &__row {
    margin: 10px 0;
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
}

/* ----- Новые минимальные стили для видео (не меняют сами видео) ----- */
.video-container {
  margin: 20px 0;
  background: #f9f9f9;
  padding: 16px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.ab__video {
  transition: box-shadow 0.2s ease;
  &:hover {
    box-shadow: 0 0 0 3px #d65460; /* акцентный цвет, не перекрывает элементы управления */
  }
}
</style>

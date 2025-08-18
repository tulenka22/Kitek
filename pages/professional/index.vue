<template>
  <block-ab title="Профессионалитет">
    <div class="block-zxc__right">
      <a class="ab__link" href="/professional"> <b>О профессионалитете</b></a>
      <a class="ab__link" href="/professional/members-cluster">
        <b>Участники образовательного кластера «Союз+»</b></a
      >
      <a class="ab__link" href="/professional/news"> <b>Новости проекта</b></a>
      <a class="ab__link" href="/professional/careerMaps"> <b>Карьерные карты</b></a>
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
          >Отель «Cronwell Park Ника» ИП Бомбин С.А
        </a>
      </li>
      <li>
        <a href="https://vk.com/club54761203?ysclid=lm4gez00jo476575976" class="ab__link"
          >ООО «Стройподряд»</a
        >
      </li>
      <li>
        <a href="https://ibisomsk.ru" class="ab__link"
          >ОАО «Гостиница «Сибирь» (гостиница ibis Omsk)</a
        >
      </li>
      <li>
        <a href="https://irtyshriviera.ru" class="ab__link">ОАО «Гостиница «Иртыш - Ривьера»</a>
      </li>
      <br />
      <br />
      <br />
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
          образования «Союз+»,</a
        >
      </li>
      <br />
      <li>
        <a href="/data/programa-d-s/otechobespechenii.pdf" class="ab__link"
          >О техническом обеспечении</a
        >
      </li>

      <!-- <li><a href="https://irtyshriviera.ru/" class="ab__link">ООО "Иртыш Ривьера"</a></li> -->
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
        <!-- <a href="https://t.me/FP_professionalitet" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconTelegram />
          </IconWrapper>
        </a> -->
      </div>
    </div>
    <div class="document-list">
      <a class="ab__link" href="/professional"> <b red>О профессионалитете</b></a>
      <a class="ab__link" href="/professional/members-cluster">
        <b red>Участники образовательного кластера «Союз+»</b></a
      >
      <a class="ab__link" href="/professional/news"> <b red>Новости проекта</b></a>
      <a class="ab__link" href="/professional/careerMaps"> <b red>Карьерные карты</b></a>
    </div>

    <a class="ab__link" href="https://япроф.рф/"
      ><img alt="Logo" target="_blank" src="/img/professional/ЛогоПроф2024.png" class="logo"
    /></a>
  </block-ab>
</template>

<script>
import Block from '~/components/app/Block.vue'
import { loadDynamic } from '~/core/helpers/file'
export default {
  components: { Block },
  data() {
    return {
      plan: null,
      swiperOptions: {
        grabCursor: true,
        autoplay: {
          enabled: true,
          delay: 5000,
        },
      },
      title: 'Приёмная комиссия',
      description:
        'Бюджетное профессиональное образовательное учреждение Омской области «Колледж инновационных технологий, экономики и коммерции». Колледж ведет подготовку по следующим Специальностям/профессиям, 09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ (КВАЛИФИКАЦИЯ – ПРОГРАММИСТ), 09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ (КВАЛИФИКАЦИЯ – РАЗРАБОТЧИК WEB И МУЛЬТИМЕДИЙНЫХ ПРИЛОЖЕНИЙ), 40.02.04 ЮРИСПРУДЕНЦИЯ, 38.02.01 ЭКОНОМИКА И БУХГАЛТЕРСКИЙ УЧЕТ (ПО ОТРАСЛЯМ), 38.02.04 КОММЕРЦИЯ (ПО ОТРАСЛЯМ), 43.02.16 ТУРИЗМ И ГОСТЕПРИИМСТВО, 38.02.05 ТОВАРОВЕДЕНИЕ И ЭКСПЕРТИЗА КАЧЕСТВА ПОТРЕБИТЕЛЬСКИХ ТОВАРОВ, 43.02.15 ПОВАРСКОЕ И КОНДИТЕРСКОЕ ДЕЛО, 43.01.09 ПОВАР, КОНДИТЕР, 26.01.09 МОТОРИСТ СУДОВОЙ, 26.02.05 ЭКСПЛУАТАЦИЯ СУДОВЫХ ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК',
      jsonPath: 'dynamic/rating/plan.json',
      table_plan: false,
      table: false,
      advantage: false,
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
  async created() {
    try {
      this.plan = JSON.parse(await loadDynamic(this.jsonPath))
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
  methods: {},
  computed: {
    specialties() {
      return this.$store.state.specialties
    },
    fpSpecialties() {
      const fpSpecialties = []
      const otherSpecialties = []

      this.specialties.forEach((specialtie) => {
        if (specialtie.group === 'ФП') {
          fpSpecialties.push(specialtie)
        } else {
          otherSpecialties.push(specialtie)
        }
      })

      return fpSpecialties
    },
    otherSpecialties() {
      const fpSpecialties = []
      const otherSpecialties = []

      this.specialties.forEach((specialtie) => {
        if (specialtie.group === 'ФП') {
          fpSpecialties.push(specialtie)
        } else {
          otherSpecialties.push(specialtie)
        }
      })

      return otherSpecialties
    },
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
</style>

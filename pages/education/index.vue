<template>
  <block-ab title="Образование">
    <div class="block-zxc__right">
      <!-- ДПО и ПО -->
      <common-documents-list json-path="documents/education-dpo.json" />
      <common-documents-list json-path="documents/education-po.json" />
    </div>
    <p class="ab__p"><b>Форма обучения:</b> очная, заочная.</p>
    <p class="ab__p">
      <b>Нормативные сроки обучения - специальности:</b>
      <ul>
        <li> &nbsp; - 9 классов: 3 года 10 месяцев; </li>
        <li> &nbsp; - 11 классов: 2 года 10 месяцев; </li>
      </ul> 
    </p>
    <p class="ab__p">
      <b>Нормативные сроки обучения - рабочие профессии:</b>
      <ul>
        <li> &nbsp; - 9 классов: 2 года 10 месяцев; </li>
      </ul> 
    </p>
    <p class="ab__p">
      Срок действия государственной аккредитации:
      <a target="_blank" href="/data/organization/Реестровая выписка (госаккредитация).pdf"
        >бессрочно</a
      >
    </p>
    <p class="ab__p">Обучение ведется на русском языке.</p>

    <h2 class="ab__subtitle">Документы</h2>
    <ul class="ab__list">
      <li>
        <a
          class="ab__link"
          target="_blank"
          href="/data/organization/Выписка из реестра лицензий № 55.12.П.22.06.2021.pdf"
          >Лицензия на право ведения образовательной деятельности с приложениями<icon-wrapper
            class="ab__icon"
            width="12"
            height="16"
            ><icon-document /></icon-wrapper
        ></a>
      </li>
      <li>
        <a
          class="ab__link"
          target="_blank"
          href="/data/educational/Сведения о численности обучающихся на 05.10.2024.pdf"
          >Сведения о численности обучающихся 2024г<icon-wrapper class="ab__icon" width="12" height="16"
            ><icon-document /></icon-wrapper
        ></a>
      </li>
      <li>
        <!-- <a
          class="ab__link"
          target="_blank"
          href="/data/educational/Результаты приемной комиссии 2023.pdf">
          Результаты приемной комиссии
          <icon-wrapper class="ab__icon" width="12" height="16"><icon-document /></icon-wrapper
        ></a> -->
      </li>
    </ul>
    <h2 class="ab__subtitle">
      <b> Рабочие программы воспитания </b> 
    </h2>
    <ul class="ab__list">
      <li class="ab__link" v-for="(education, id) of educations" :key="id">
        <a target="_blank" :href="education.url">{{ education.name }}</a>
      </li>
    </ul>

      <h2 class="ab__subtitle">Сведения о реализации образовательных программ по специальностям/профессиям, реализуемым в рамках федерального проекта «Профессионалитет»:</h2>
    <ul class="ab__list" v-for="spec in specialtesFP" :key="spec.name">
      <li>
        <b red>{{ spec.name }}</b>
      </li>
      <p class="ab__p">Форма обучения: {{ spec.formOfEducation }}</p>
      <p class="ab__p">Срок обучения: {{ spec.period }}</p>
      <a v-if="spec.plan21" :href="spec.plan21" target="_blank" class="ab__p ab__link">
        Учебный план, 2021 г.
      </a>
      <a v-if="spec.planIX21" :href="spec.planIX21" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов) 2021 г.
      </a>
      <a v-if="spec.planXI21" :href="spec.planXI21" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов) 2021 г.
      </a>
      <a v-if="spec.plan" :href="spec.plan" target="_blank" class="ab__p ab__link">
        Учебный план, 2023 г.
      </a>
      <a v-if="spec.planIX" :href="spec.planIX" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов) 2023 г.
      </a>
      <a v-if="spec.planXI" :href="spec.planXI" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов) 2023 г.
      </a>
      <a v-if="spec.planZ" :href="spec.planZ" target="_blank" class="ab__p ab__link">
        Учебный план (заочное) 2023 г.
      </a>
      <a v-if="spec.plan2024" :href="spec.plan2024" target="_blank" class="ab__p ab__link">
        Учебный план, 2024 г.
      </a>
      <a v-if="spec.plan20249" :href="spec.plan20249" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов) 2024 г.
      </a>
      <a v-if="spec.plan202411" :href="spec.plan202411" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов) 2024 г.
      </a>
      <a v-if="spec.plan20249z" :href="spec.plan20249z" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов заочное) 2024 г.
      </a>
      <a v-if="spec.plan202411z" :href="spec.plan202411z" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов заочное) 2024 г.
      </a>
      <a v-if="spec.plan20242" :href="spec.plan20242" target="_blank" class="ab__p ab__link">
        Учебный план, 2024 г.
      </a>



      <a v-if="spec.ttg11" :href="spec.ttg11" target="_blank" class="ab__p ab__link">
        РПВ воспитания 2024 г.
      </a>
      <a v-if="spec.tdd11" :href="spec.tdd11" target="_blank" class="ab__p ab__link">
        РПВ воспитания 2024 г.
      </a>



      <p class="ab__p" v-if="spec.plan == ''">Учебный план</p>
      <p class="ab__p" v-if="spec.eduprocess == ''">Календарный учебный график</p>
      <a v-if="spec.eduprocess" :href="spec.eduprocess" target="_blank" class="ab__p ab__link">
        Календарный учебный график
      </a>
      <a
        v-if="spec.educationProgram"
        :href="spec.educationProgram"
        target="_blank"
        class="ab__p ab__link">
        Образовательная программа подготовки специалистов среднего звена
      </a>
      <p class="ab__p" v-if="spec.educationProgram == ''">
        Образовательная программа подготовки специалистов среднего звена
      </p>
      <a
        v-if="spec.educationProgram2"
        :href="spec.educationProgram2"
        target="_blank"
        class="ab__p ab__link">
        Образовательная программа подготовки специалистов среднего звена
      </a>
      <p class="ab__p" v-if="spec.educationProgram2 == ''">
        Образовательная программа подготовки специалистов среднего звена
      </p>
      </ul>

    <h2 class="ab__subtitle">Сведения о реализации образовательных программ:</h2>
    <ul class="ab__list" v-for="spec in specialtesOther" :key="spec.name">
      <li>
        <b red>{{ spec.name }}</b>
      </li>
      <p class="ab__p">Форма обучения: {{ spec.formOfEducation }}</p>
      <p class="ab__p">Срок обучения: {{ spec.period }}</p>
      <a v-if="spec.plan21" :href="spec.plan21" target="_blank" class="ab__p ab__link">
        Учебный план 2021 г.
      </a>
      <a v-if="spec.planIX21" :href="spec.planIX21" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов) 2021 г.
      </a>
      <a v-if="spec.planXI21" :href="spec.planXI21" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов) 2021 г.
      </a>
      <a v-if="spec.plan" :href="spec.plan" target="_blank" class="ab__p ab__link">
        Учебный план 2023 г.
      </a>
      <a v-if="spec.planIX" :href="spec.planIX" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов) 2023 г.
      </a>
      <a v-if="spec.planXI" :href="spec.planXI" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов) 2023 г.
      </a>
      <a v-if="spec.planZ" :href="spec.planZ" target="_blank" class="ab__p ab__link">
        Учебный план (заочное) 2023 г.
      </a>
      <a v-if="spec.plan2024" :href="spec.plan2024" target="_blank" class="ab__p ab__link">
        Учебный план 2024 г.
      </a>
      <a v-if="spec.plan20249" :href="spec.plan20249" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов) 2024 г.
      </a>
      <a v-if="spec.plan202411" :href="spec.plan202411" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов) 2024 г.
      </a>
      <a v-if="spec.plan20249z" :href="spec.plan20249z" target="_blank" class="ab__p ab__link">
        Учебный план (9 классов заочное) 2024 г.
      </a>
      <a v-if="spec.plan202411z" :href="spec.plan202411z" target="_blank" class="ab__p ab__link">
        Учебный план (11 классов заочное) 2024 г.
      </a>
      <p class="ab__p" v-if="spec.plan == ''">Учебный план</p>
      <p class="ab__p" v-if="spec.eduprocess == ''">Календарный учебный график</p>
      <a v-if="spec.eduprocess" :href="spec.eduprocess" target="_blank" class="ab__p ab__link">
        Календарный учебный график
      </a>
            <a v-if="spec.yyou6" :href="spec.yyou6" target="_blank" class="ab__p ab__link">
        РПВ воспитания 2024 г.
      </a>
        


      <a
        v-if="spec.educationProgram"
        :href="spec.educationProgram"
        target="_blank"
        class="ab__p ab__link">
        Образовательная программа подготовки специалистов среднего звена
      </a>
      <p class="ab__p" v-if="spec.educationProgram == ''">
        Образовательная программа подготовки специалистов среднего звена
      </p>
      </ul>

      <ul class="ab__list">
        <li>
          <b red>О трудоустройстве выпусников</b>
        </li>
        <a
      class="ab__link"
      target="_blank"
      href="/data/assistance/Трудоустройство выпускников 2020-2022 г.pdf"
      ><icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        >Трудоустройство выпускников 2020-2022 год</a>
      </ul>

    <common-documents-list class="document-list" json-path="documents/education-dpo.json" />
    <common-documents-list class="document-list" json-path="documents/education-po.json" />
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  data() {
    return {
      specialtes: [],
      title: 'Образование',
      description:
        'Информация по образовательным программам, срокам аккредитации, численности студентов, сведения об образовательной деятельности.',

      educations: [
        {
          name: '43.02.15 Поварское и кондитерское дело',
          url: '/data/educational/43.02.15 Поварское и кондитерское дело.pdf',
        },
        {
          name: '43.02.14 Гостиничное дело',
          url: '/data/educational/43.02.14 Гостиничное дело.pdf',
        },
        {
          name: '43.01.09 Повар, кондитер',
          url: '/data/educational/43.01.09 Повар, кондитер.pdf',
        },
        {
          name: '40.02.01 Право и организация социального обеспечения',
          url: '/data/educational/40.02.01 Право и организация социального обеспечения.pdf',
        },
        {
          name: '38.02.05 Товароведение и экспертиза качества потребительских товаров',
          url: '/data/educational/38.02.05 Товароведение и экспертиза качества потребительских товаров.pdf',
        },
        {
          name: '38.02.04 Коммерция (по отраслям)',
          url: '/data/educational/38.02.04 Коммерция (по отраслям).pdf',
        },
        {
          name: '38.02.01 Экономика и бухгалтерский учет по отраслям',
          url: '/data/educational/38.02.01 Экономика и бухгалтерский учет по отраслям.pdf',
        },
        {
          name: '26.02.05 Эксплуатация судовых энергетических установок',
          url: '/data/educational/26.02.05 Эксплуатация судовых энергетических установок.pdf',
        },
        {
          name: '26.01.10 Механик маломерного судна',
          url: '/data/educational/26.01.10 Механик маломерного судна.pdf',
        },
        {
          name: '26.01.09 Моторист судовой',
          url: '/data/educational/26.01.09 Моторист судовой.pdf',
        },
        {
          name: '09.02.07 Информационные системы и программирование',
          url: '/data/educational/09.02.07 Информационные системы и программирование.pdf',
        },
      ],
    }
  },
  computed: {
    specialtesTrue: function () {
      // Фильтрация специальностей по группе "ФП"
      const specialtesFP = this.specialtes.filter(function (specialte) {
        return specialte.group === 'ФП'
      })
      // Фильтрация остальных специальностей
      const specialtesOther = this.specialtes.filter(function (specialte) {
        return specialte.group !== 'ФП'
      })
      // Конкатенация фильтрованных массивов
      return specialtesFP.concat(specialtesOther)
    },
    specialtesFP: function () {
      return this.specialtes.filter(function (specialte) {
        return specialte.group === 'ФП'
      })
    },
    specialtesOther: function () {
      return this.specialtes.filter(function (specialte) {
        return specialte.group !== 'ФП'
      })
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
      this.specialtes = JSON.parse(await loadDynamic('dynamic/specs/specs.json'))
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
}
</script>
<style scoped lang="scss">
.ab {
  &__icon {
    color: $primary-color;
    display: inline;
  }
}
</style>

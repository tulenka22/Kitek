<template>
  <block-ab title="Образовательные стандарты">
    <p class="ab__p">
      Федеральные государственные образовательные стандарты (ФГОС) представляют собой совокупность
      требований, обязательных при реализации основных образовательных программ начального общего,
      основного общего, среднего общего, среднего профессионального и высшего образования
      образовательными учреждениями, имеющими государственную аккредитацию.
    </p>
    <ul class="ab__list">
      <li class="ab__link" v-for="(edu, idx) of educations" :key="idx">
        <a target="_blank" :href="edu.url">{{ edu.name }}</a>
      </li>
      <li class="ab__link">
        <a class="ab__link" target="_blank" href="/data/obrazovatel/Юриспруденция.pdf"
          >40.02.04 Юриспруденция</a
        >
      </li>
      <li class="ab__link">
        <a href="/data/obrazovatel/Торговоедело.pdf">38.02.08 Торговое дело</a>
      </li>
    </ul>
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      educations: [
        {
          name: '38.02.04 Коммерция (по отраслям)',
          url: 'https://base.garant.ru/70687350/53f89421bbdaf741eb2d1ecc4ddb4c33/',
        },
        {
          name: '38.02.05 Товароведение и экспертиза качества потребительских товаров',
          url: 'https://base.garant.ru/70734886/53f89421bbdaf741eb2d1ecc4ddb4c33/',
        },
        {
          name: '38.02.01 Экономика и бухгалтерский учет (по отраслям)',
          url: 'https://base.garant.ru/71887436/53f89421bbdaf741eb2d1ecc4ddb4c33/',
        },
        {
          name: '43.02.16 Туризм и гостеприимство',
          url: '/data/educational/43.02.16 ФГОС ТиГ.pdf',
        },
        {
          name: '43.02.15 Поварское и кондитерское дело',
          url: 'https://www.garant.ru/products/ipo/prime/doc/71471434/',
        },
        {
          name: '43.02.14 Гостиничное дело',
          url: 'https://www.garant.ru/products/ipo/prime/doc/71477694/',
        },
        {
          name: '09.02.07 Информационные системы и программирование',
          url: 'https://www.garant.ru/products/ipo/prime/doc/71477324/',
        },
        {
          name: '40.02.01 Право и организация социального обеспечения',
          url: 'https://base.garant.ru/70710002/53f89421bbdaf741eb2d1ecc4ddb4c33/',
        },
        {
          name: '43.01.09 Повар, кондитер',
          url: 'https://www.garant.ru/products/ipo/prime/doc/71476300/',
        },
        {
          name: '26.01.09 Моторист судовой',
          url: 'https://base.garant.ru/70444498/53f89421bbdaf741eb2d1ecc4ddb4c33/ ',
        },
        {
          name: '26.02.05 Эксплуатация судовых энергетических установок',
          url: 'https://base.garant.ru/70691022/53f89421bbdaf741eb2d1ecc4ddb4c33/',
        },
      ],
    }
  },
}
</script>

<style scoped lang="scss"></style>

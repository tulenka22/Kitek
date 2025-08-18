<template>
  <div class="projects">
    <AppBlock
      :without-body="true"
      :block-style="{ padding: 0 }"
      title="Проекты"
      class="projects__self" />
    <main class="projects__content">
      <EntitiesProjectCard v-for="(project, idx) of projects" :key="idx" :instance="project" />
    </main>
  </div>
</template>

<script>
export default {
  name: 'BlockProjects',
  data() {
    return {
      projects: [
        {
          title: 'Мастерские',
          description:
            'Структурное подразделение колледжа, оснащённое современной материально-технической базой для <br/>обеспечения практической<br/> подготовки обучающихся',
          img: 'img/projects/workshop.png',
          imgStyle: { height: '100px', width: '100px' },
          link: '/projects/workshop',
        },
        {
          title: 'Билет в будущее',
          description:
            'Федерального проект по ранней профессиональной ориентации<br/> учащихся 6-11-х классов общеобразовательных<br/> организаций',
          img: 'img/projects/futureTicket.svg',
          imgStyle: {
            height: '80px',
            width: '80px',
            bottom: '16px',
            right: '16px',
          },
          link: '/projects/ticket',
        },
        {
          title: 'Демонстрационный экзамен',
          description:
            'Это форма государственной итоговой аттестации выпускников, которая<br/> позволяет в условиях, приближенных к производственным, продемонстрировать освоенные профессиональные компетенции.',
          img: 'img/projects/demoekz.webp',
          imgStyle: {
            height: '120px',
            width: '150px',
            transform: 'rotate(-35deg)',
          },
          link: '/projects/demo-ekzam',
        },
        {
          title: 'Содействие занятости',
          description:
            'Помощь гражданам в трудоустройстве или в самостоятельной профессиональной<br/> деятельности',
          img: 'img/projects/sodeistv.svg',
          imgStyle: {
            height: '120px',
            width: '150px',
            transform: 'rotate(-35deg)',
          },
          link: '/projects/promotion',
        },
        {
          title: 'Год педагога и наставника',
          description:
            'Миссия Года – признание особого статуса педагогических работников, в том числе выполняющих наставническую деятельность.',
          img: 'img/projects/GPiN.png',
          imgStyle: {
            height: '120px',
            width: '150px',
          },
          link: '/organization/mentor',
        },
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.projects {
  margin-top: 60px;
  &__content {
    margin-top: 16px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 16px;
    @include medium-media {
      display: block;
      &::v-deep .card {
        margin-top: 16px;
      }
    }
  }
}
</style>

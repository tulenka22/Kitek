<template>
  <div class="educational-complex">
    <block-ab title="Учебно-производственный комплекс">
      <div class="content">
        <p class="intro">
          Учебно-производственный комплекс в форме учебно-производственного предприятия (столовая) 
          (далее – УПП), функционирует в БПОУ "КИТЭК" более 30 лет, являясь производственной базой 
          для реализации практической подготовки по профессии 43.01.09 Повар, кондитер и специальности 
          43.02.15 Поварское и кондитерское дело.
        </p>

        <p>
          Деятельность УПП направлена на формирование механизма взаимодействия между рынком труда, 
          системой образования и работодателями, подготовку и переподготовку высококвалифицированных 
          кадров, в том числе создание условий для стажировки преподавателей колледжа.
        </p>

        <div class="statistics">
          <p>
            <strong>В 2024-2025 уч. г.</strong> на базе УПП прошли учебную и производственную практики 
            <span class="highlight">190 человек</span>, на <strong>2025-2026 уч.г.</strong> запланирована 
            практическая подготовка <span class="highlight">более 700 обучающихся</span>.
          </p>
          <p>
            По итогам 2024 г. результат от приносящей доход деятельности УПП составил 
            <span class="highlight">2 млн. 900 тыс. руб.</span>
          </p>
        </div>

        <div class="fp-section">
          <h3>В рамках реализации ФП "Профессионалитет" УПК функционирует с 01.09.2025, для чего созданы следующие условия:</h3>
          <ol class="conditions-list">
            <li>
              В штатном расписании выделено структурное подразделение – 6 ставок, которым управляет 
              руководитель отдела "Учебно-производственный комплекс".
            </li>
            <li>
              Разработано Положение об учебно-производственном комплексе, которое рассмотрено на 
              Педагогическом Совете 29.08.2025 и будет согласовано на заседании Управляющей компании.
            </li>
            <li>
              В зонах по видам работ реализуются обновленные программы дополнительного профессионального 
              образования, в которых спикерами и лидерами общественного мнения выступают работодатели кластера.
            </li>
            <li>
              В штате УПК работают, помимо штатных сотрудников колледжа, действующий бренд-шеф и су-шеф 
              омских ресторанов.
            </li>
            <li>
              Помимо развития профессиональных компетенций одной из задач УПК является подготовка выпускника, 
              который может сам определять свою судьбу через формирование новой совокупности экзистенциальных 
              навыков (сила воли, самосознание, способность к саморефлексии, саморазвитию).
            </li>
          </ol>
        </div>
      </div>
            <div class="document-section">
        <h3>Документы</h3>
        <div class="documents">
          <b red>
            <a class="ab__link doc-link" target="_blank" href="/data/predp/П_СМК_03_5_52_2024_Ответственность_руководства_Положение_о_УПК.pdf">
              <icon-wrapper class="ab__icon" width="18" height="22"><icon-document /></icon-wrapper>Положение об учебно-производственном комплексе
            </a>
          </b>
        </div>
      </div>
      <div class="img-cont">
        <div class="img-container">
          <img class="img-single__minimg" src="/img/predp/1.webp" />
          <img class="img-single__minimg" src="/img/predp/2.webp" />
        </div>
        <div class="img-container">
          <img class="img-single__minimg" src="/img/predp/3.webp" />
        </div>
      </div>

    </block-ab>
  </div>
</template>

<style scoped>
.educational-complex {

  line-height: 1.6;
  color: #333;
}

.content {
  max-width: 1200px;

}

.intro {
  font-size: 1.1em;
  margin-bottom: 20px;
  text-align: justify;
}

.statistics {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 20px;
  border-radius: 10px;
  margin: 25px 0;
  border-left: 4px solid #c43e3e;
}

.statistics p {
  margin: 10px 0;
}

.highlight {
  background-color: #ffeaa7;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: bold;
  color: #c43e3e;
}

.fp-section {
  margin: 30px 0;
  padding: 25px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.fp-section h3 {
  color: #2c3e50;
  margin-bottom: 20px;
  font-size: 1.2em;
}

.conditions-list {
  padding-left: 20px;
}

.conditions-list li {
  margin-bottom: 15px;
  padding-left: 10px;
  text-align: justify;
}

.conditions-list li::marker {
  color: #e74c3c;
  font-weight: bold;
}

.document-section {
  margin-top: 40px;
  padding: 25px;

  border-radius: 10px;

}

.img-cont {
  margin: 10px 0;
  padding: 25px;

  border-radius: 8px;

}

.document-section h3 {
  margin-bottom: 20px;
  font-size: 1.3em;
}

.documents {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.doc-link {

  text-decoration: none;

  background-color: rgba(255,255,255,0.2);
  border-radius: 6px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 10px;
}

.doc-link:hover {
  background-color: rgba(255,255,255,0.3);
  transform: translateX(5px);
  text-decoration: underline;
}

.img-single__minimg {
  border-radius: 10px;
}

@media (max-width: 768px) {
  .content {
    padding: 15px;
  }
  
  .statistics,
  .fp-section,
  .document-section {
    padding: 15px;
  }
  
  .conditions-list {
    padding-left: 15px;
  }
}
</style>
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { VacancyComponent } from '../vacancy/vacancy.component';
import { Vacancy } from '../app.model';
import { AppService } from '../app.services';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule, VacancyComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  vacancies !: Vacancy[];
  loaded = false;
  constructor(private route: ActivatedRoute,
    private appService: AppService) {

  }
  ngOnInit(): void {
    this.appService.getTopTenVacancy().subscribe((vacancies) => {
      this.vacancies = vacancies;
      this.loaded = true;
    })
  }
}

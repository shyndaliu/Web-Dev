import { Component, Input } from '@angular/core';
import { Vacancy } from '../app.model';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vacancy',
  standalone: true,
  imports: [VacancyComponent, CommonModule],
  templateUrl: './vacancy.component.html',
  styleUrl: './vacancy.component.css'
})
export class VacancyComponent {
  @Input() vacancy!: Vacancy;

}

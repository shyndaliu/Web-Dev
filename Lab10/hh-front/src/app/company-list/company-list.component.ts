import { Component, OnInit } from '@angular/core';
import { Company } from '../app.model';
import { AppService } from '../app.services';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './company-list.component.html',
  styleUrl: './company-list.component.css'
})
export class CompanyListComponent implements OnInit {
  companies !: Company[];
  constructor(
    private appService: AppService) {

  }
  ngOnInit() {
    this.appService.getCompanies().subscribe((companies) =>
      this.companies = companies)
  }

}

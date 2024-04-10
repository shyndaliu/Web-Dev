import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CompanyListComponent } from './company-list/company-list.component';
import { CompanyComponent } from './company/company.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent, title: 'HeadHunter' },
    { path: 'companies', component: CompanyListComponent, title: 'Companies' },
    { path: 'companies/:id', redirectTo: 'companies/:id/vacancies' },
    { path: 'companies/:id/vacancies', component: CompanyComponent, title: 'Company' },

];

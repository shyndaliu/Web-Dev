import { Component, Input, OnInit } from '@angular/core';
import { trigger, transition, style, animate } from '@angular/animations';

import { categories } from '../categories';
import { Product } from '../product';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
  animations: [
    trigger('fadeInOut', [
      transition(':enter', [
        style({ opacity: 0 }),
        animate('300ms', style({ opacity: 1 })),
      ]),
      transition(':leave', [
        animate('300ms', style({ opacity: 0 }))
      ])
    ])
  ]
})
export class ProductListComponent {
  @Input() categoryId: number = 0;
  products: Product[] = [];
  ngOnInit(): void {
    this.loadProducts();
  }

  private loadProducts(): void {
    const ps: Product[] = [];
    const categoryProducts = categories[this.categoryId].products;
    for (const product of categoryProducts) {
      ps.push(new Product(product.id, product.name, product.price, product.description, product.likes, product.img, product.link));
    }
    this.products = ps;
    console.log(this.categoryId);
  }
  onProductRemove(id: number) {
    this.products = this.products.filter((product) => product.id !== id);
  }


}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
import {Component} from '@angular/core';

import {products} from '../products';

@Component({
    selector: 'app-product-list',
    templateUrl: './product-list.component.html',
    styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
    products = [...products];

    share(text: string) {
        navigator.clipboard.writeText(text).then(function () {
            console.log('Async: Copying to clipboard was successful!');
            window.open('https://web.telegram.org/k/', '_blank');
        }, function (err) {
            console.error('Async: Could not copy text: ', err);
        });

    }
}

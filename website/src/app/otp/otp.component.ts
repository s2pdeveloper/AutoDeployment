import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-otp',
  templateUrl: './otp.component.html',
  styleUrls: ['./otp.component.scss']
})
export class OtpComponent {
  constructor(private routes: Router) {}
  navigateTo(path: any) {
    this.routes.navigate([path]);
  }
}

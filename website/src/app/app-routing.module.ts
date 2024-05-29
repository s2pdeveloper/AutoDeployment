import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OtpComponent } from './otp/otp.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path:'', redirectTo: 'login', pathMatch: 'full'},
  {
    path:'login',component:LoginComponent
  },
  {
    path:'otp',component:OtpComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

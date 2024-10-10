import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AdminRoutingModule } from './admin-routing.module';
import { UserComponent } from './pages/user/user.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { RightsComponent } from './pages/rights/rights.component';

@NgModule({
  declarations: [DashboardComponent, RightsComponent, UserComponent],
  imports: [CommonModule, AdminRoutingModule],
})
export class AdminModule {}
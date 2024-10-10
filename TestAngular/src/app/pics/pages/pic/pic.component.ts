import { Component } from '@angular/core';
import { catchError } from 'rxjs';
import { NgForm } from '@angular/forms';
import { IPic } from '../../../core/interfaces/i-pic';
import { PicService } from '../../../core/services/pic.service';

@Component({
  selector: 'app-pic',
  templateUrl: './pic.component.html',
  styleUrl: './pic.component.css',
})
export class PicComponent {
  pic?: IPic;
  file: any;

  constructor(private picService: PicService) {}

  onSubmit(form: NgForm) {
    if (form.valid) {
      this.picService
        .upload(this.file)
        .pipe(catchError(this.picService.baseHttp.handleError))
        .subscribe((resp: IPic) => {
          this.pic = resp;
        });
    }
  }

  upload(event: any) {
    this.file = event.target.files[0];
  }
}

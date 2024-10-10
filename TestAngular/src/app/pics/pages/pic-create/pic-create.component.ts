import { Component } from '@angular/core';
import { IPic } from '../../../core/interfaces/i-pic';
import { catchError } from 'rxjs';
import { NgForm } from '@angular/forms';
import { PicService } from '../../../core/services/pic.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-pic-create',
  templateUrl: './pic-create.component.html',
  styleUrl: './pic-create.component.css',
})
export class PicCreateComponent {
  pic?: IPic;
  file: any;

  constructor(private picService: PicService, private router: Router) {}

  onSubmit(form: NgForm) {
    if (form.valid) {
      this.picService
        .upload(this.file)
        .pipe(
          catchError((error) => {
            const errorMessage =
              error?.error?.src?.[0] || 'An error occurred during upload.';
            Swal.fire({
              title: 'Upload Error',
              text: errorMessage,
              icon: 'error',
            });
            return [];
          })
        )
        .subscribe((resp: IPic) => {
          Swal.fire({
            title: 'Success',
            text: 'Upload successfully!',
            icon: 'success',
          });

          this.pic = resp;
          this.router.navigate(['/pic']);
        });
    }
  }

  upload(event: any) {
    this.file = event.target.files[0];
  }
}

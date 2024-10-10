import { Component, OnInit } from '@angular/core';
import { IPic } from '../../../core/interfaces/i-pic';
import { PicService } from '../../../core/services/pic.service';
import { ActivatedRoute, Router } from '@angular/router';
import { catchError } from 'rxjs';
import { NgForm } from '@angular/forms';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-pic-detail',
  templateUrl: './pic-detail.component.html',
  styleUrl: './pic-detail.component.css',
})
export class PicDetailComponent implements OnInit {
  pic!: IPic;
  file: any;
  id: number = 0;

  constructor(
    private picService: PicService,
    private activatedRoute: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.id = parseInt(this.activatedRoute.snapshot.paramMap.get('id') || '0');
    this.picService
      .getPic(this.id)
      .pipe(catchError(this.picService.baseHttp.handleError))
      .subscribe((resp: IPic) => {
        this.pic = resp;
      });
  }

  onSubmit(form: NgForm) {
    if (form.valid) {
      this.picService
        .updatePic(this.id, this.file)
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
            text: 'Edit successfully!',
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

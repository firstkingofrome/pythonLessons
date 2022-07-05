	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 11, 0	sdk_version 12, 1
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16                     ; =16
	.cfi_def_cfa_offset 16
	mov	w0, #0
	str	wzr, [sp, #12]
	mov	w8, #3
	str	w8, [sp, #8]
	mov	w8, #4
	str	w8, [sp, #4]
	ldr	w8, [sp, #8]
	ldr	w9, [sp, #4]
	mul	w8, w8, w9
	ldr	w9, [sp, #8]
	mul	w8, w8, w9
	ldr	w9, [sp, #4]
	mul	w8, w8, w9
	str	w8, [sp, #4]
	add	sp, sp, #16                     ; =16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols

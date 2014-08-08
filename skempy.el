;;; @export "defun"
(defun sks-execute-python-test()
  (interactive)
  (let ((test-method (shell-command-to-string (format "skempy-find-test %s %d" (buffer-file-name) (line-number-at-pos)))))
    (compile (concat "python -m unittest " test-method)))
  )
;;; @export "key-binding"
(add-hook 'python-mode-hook
          '(lambda () (local-set-key [C-f7] 'sks-execute-python-test)))

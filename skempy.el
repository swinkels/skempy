(defun sks-execute-python-test()
  (interactive)
  (let ((test-method (shell-command-to-string (format "skempy-find-test %s %d" (buffer-file-name) (line-number-at-pos)))))
    (compile (concat "python -m unittest " test-method)))
  )

(add-hook 'python-mode-hook
          '(lambda ()
             (local-set-key [C-f7] 'sks-execute-python-test)
             (fset 'sks-build 'sks-execute-python-test)))
  
(defun sks-recompile()
  "Redo the last compilation when appropriate.

When the compilation buffer *compilation* exist, this command
switches to that buffer and executes the recompile command.

If the compilation buffer does not exist but buffer-local
variable sks-build does, this command executes the command stored
by sks-build, otherwise it does nothing."
  (interactive)
  (let ((compilation-buffer (get-buffer "*compilation*")))
    (if compilation-buffer
        (progn
          (pop-to-buffer compilation-buffer)
          (recompile))
      (if (functionp 'sks-build)
          (sks-build)
        (message "[sks-project] No *compilation* buffer exists and no sks-build command is defined"))))
  )
